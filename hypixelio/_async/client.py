__all__ = "AsyncClient"

import asyncio
import random
import typing as t

import aiohttp
import aiohttp_client_cache
from aiohttp_client_cache.backends import (
    CacheBackend,
    MongoDBBackend,
    RedisBackend,
    SQLiteBackend,
)

from ..base import BaseClient
from ..exceptions import (
    GuildNotFoundError,
    HypixelAPIError,
    InvalidArgumentError,
    PlayerNotFoundError,
    RateLimitError,
)
from ..models import (
    boosters,
    caching,
    find_guild,
    friends,
    games,
    guild,
    key,
    leaderboard,
    player,
    player_status,
    recent_games,
    skyblock,
    watchdog,
)
from ..utils.constants import HYPIXEL_API, TIMEOUT
from ..utils.url import form_url


class AsyncClient(BaseClient):
    """
    The client for this wrapper, that handles the requests, authentication, loading and usages of the end user.

    Examples
    --------
    Import the async client first.

        >>> from hypixelio._async import AsyncClient

    If you have a single API key, Here's how to authenticate

        >>> client = AsyncClient(api_key="123-456-789")

    You can use multiple API keys to authenticate too. (Better option for load balancing)

        >>> client = AsyncClient(api_key=["123-456", "789-000", "568-908"])

    The caching is supported inbuilt, and can be enabled easily. Here's how,
        >>> client = AsyncClient(cache=True)

    You have the option to configure cache too,
        >>> from hypixelio.models.caching import Caching, CacheBackend
        >>> cache_cfg = Caching(cache_name="my-cache", backend=CacheBackend.sqlite, expire_after=10)
        >>> client = AsyncClient(cache=True, cache_config=cache_cfg)

    You can also manipulate the cache object by accessing using the attribute `cache` And call methods as needed.
        >>> client.cache
    """

    def __init__(
        self,
        api_key: t.Union[str, list],
        cache: bool = False,
        cache_config: caching.Caching = None,
    ) -> None:
        """
        Parameters
        ----------
        api_key: t.Union[str, list]
            The API key generated in Hypixel server using the `/api new` command.
        cache: t.Optional[bool]
            Should caching be enabled.
        cache_config: t.Optional[caching.Caching]
            The configurations settings for caching, if enabled. Defaults to None.
        """
        super().__init__(api_key)

        self._uses_cache = cache
        self._cache_backend_mapping = {
            "sqlite": SQLiteBackend,
            "redis": RedisBackend,
            "mongodb": MongoDBBackend,
            "others": CacheBackend
        }

        if cache:
            if cache_config is None:
                cache_config = caching.Caching(expire_after=30, old_data_on_error=True)

            if cache_config.backend in self._cache_backend_mapping:
                backend = self._cache_backend_mapping[cache_config.backend]
                self.cache = backend(
                    cache_name=cache_config.cache_name,
                    expire_after=cache_config.expire_after
                )
            else:
                self.cache = CacheBackend(
                    cache_name=cache_config.cache_name,
                    expire_after=cache_config.expire_after,
                )

        self.__session = None
        self.__lock = asyncio.Lock()

    async def close(self) -> None:
        """Close the AIOHTTP sessions to prevent memory leaks."""
        if self.__session is not None:
            await self.__session.close()

    async def _fetch(self, url: str, data: dict = None, api_key: bool = True) -> dict:
        """
        Fetch the JSON response from the API along with the ability to include GET request parameters and support
        Authentication using API key too.

        Parameters
        ----------
        url: str
            The URL to be accessed from the API root URL.
        data: t.Optional[dict]
            The GET Request's Key-Value Pair. Example: {"uuid": "abc"} is converted to `?uuid=abc`. Defaults to None.
        api_key: bool
            If key is needed for the endpoint.

        Returns
        -------
        t.Tuple[dict, bool]
            The JSON response obtained after fetching the API, along with success value in the response.
        """
        if not self.__session:
            if not self._uses_cache:
                self.__session = aiohttp.ClientSession()
            else:
                self.__session = aiohttp_client_cache.CachedSession(cache=self.cache)

        # Check if ratelimit is hit
        if self._is_ratelimit_hit():
            raise RateLimitError(f"Retry after {self.retry_after}")

        if not data:
            data = {}

        # Assign a random key
        if api_key:
            self.headers["API-Key"] = random.choice(self._api_key)

        url = form_url(HYPIXEL_API, url, data)

        async with self.__lock:
            async with self.__session.get(url, headers=self.headers, timeout=TIMEOUT) as response:
                # 404 handling
                if response.status == 429:
                    raise HypixelAPIError(reason="The route specified does not exist.")

                # 429 status code handling
                if response.status == 429:
                    self._handle_ratelimit(response.headers)

                # 403 Status code handling
                if response.status == 403:
                    raise HypixelAPIError(reason="Invalid key specified!")

                if api_key and "RateLimit-Limit" in response.headers:
                    self._update_ratelimit(response.headers)

                try:
                    json = await response.json()
                except Exception as exception:
                    raise HypixelAPIError(f"{exception}")
                else:
                    if not json["success"]:
                        self._handle_api_failure(json)

                    return json

    async def get_key_info(self, api_key: t.Optional[str] = None) -> key.Key:
        """
        Get info about a specific Hypixel API key.

        Parameters
        ----------
        api_key: t.Optional[str]
            The API key generated in Hypixel server using the `/api new` command. Defaults to pre-specified keys.

        Returns
        -------
        key.Key
            The Key object created for the API key specified.
        """
        if not api_key:
            api_key = random.choice(self._api_key)

        json = await self._fetch(self.url["api_key"], {"key": api_key})
        return key.Key(json["record"])

    async def get_boosters(self) -> boosters.Boosters:
        """
        Get the Hypixel coin boosters, and all the info about them.

        Returns
        -------
        boosters.Boosters
            The boosters object, with all the info from the API.
        """
        json = await self._fetch(self.url["boosters"])

        return boosters.Boosters(json["boosters"], json)

    async def get_player(
        self, name: t.Optional[str] = None, uuid: t.Optional[str] = None
    ) -> player.Player:
        """
        Get all info about a Hypixel player using his username or his player UUID.

        Parameters
        ----------
        name: t.Optional[str]
            The Optional string value for the Username. Defaults to None.
        uuid: t.Optional[str]
            The Optional string Value to the UUID. Defaults to None.

        Returns
        -------
        player.Player
            The player object with all the info obtained from the API.
        """
        uuid = self._filter_name_uuid(name, uuid)
        json = await self._fetch(self.url["player"], {"uuid": uuid})

        if not json["player"]:
            raise PlayerNotFoundError("Null Value is returned", name)

        return player.Player(json["player"])

    async def get_friends(
        self, name: t.Optional[str] = None, uuid: t.Optional[str] = None
    ) -> friends.Friends:
        """
        Get the friends, and all their info of specified Hypixel player.

        Parameters
        ----------
        name: t.Optional[str]
            The Optional string value for the Username of a hypixel player. Defaults to None.
        uuid: t.Optional[str]
            The UUID of a Certain Hypixel Player. Defaults to None.

        Returns
        -------
        friends.Friends
            The Friend object with all info from the API.
        """
        uuid = self._filter_name_uuid(name, uuid)
        json = await self._fetch(self.url["friends"], {"uuid": uuid})

        return friends.Friends(json["records"])

    async def get_watchdog_info(self) -> watchdog.Watchdog:
        """
        Get all the stats about the Watchdog (Punishment stats) for the last few days/

        Returns
        -------
        watchdog.Watchdog
            The Watchdog object with all the info.
        """
        json = await self._fetch(self.url["watchdog"])

        return watchdog.Watchdog(json)

    async def get_guild(
        self, name: t.Optional[str] = None, uuid: t.Optional[str] = None
    ) -> guild.Guild:
        """
        Get info about a specific Hypixel guild using the Name, or the Guild's UUID.

        Parameters
        ----------
        name: t.Optional[str]
            The Name of the Guild. Defaults to None.
        uuid: t.Optional[str]
            The ID Of the guild. Defaults to None.

        Returns
        -------
        guild.Guild
            The Guild object with the info fetched from the API.
        """
        if uuid:
            json = await self._fetch(self.url["guild"], {"id": uuid})
        elif name:
            json = await self._fetch(self.url["guild"], {"name": name})
        else:
            raise InvalidArgumentError(
                "Please provide a Named argument of the guild's Name or guild's ID."
            )

        if not json["guild"]:
            raise GuildNotFoundError("Return Value is null")
        return guild.Guild(json["guild"])

    async def get_games_info(self) -> games.Games:
        """
        Get the list of all Hypixel games, and their info.

        Returns
        -------
        games.Games
            The Games object with all the info.
        """
        json = await self._fetch(self.url["game_info"])

        return games.Games(json["games"], json["playerCount"])

    async def get_leaderboards(self) -> leaderboard.Leaderboard:
        """
        Get the leaderboard for the Hypixel games with their info.

        Returns
        -------
        leaderboard.Leaderboard
            The Leaderboard object with all info.
        """
        json = await self._fetch(self.url["leaderboards"])

        return leaderboard.Leaderboard(json["leaderboards"])

    async def find_guild(
        self, guild_name: t.Optional[str] = None, player_uuid: t.Optional[str] = None
    ) -> find_guild.FindGuild:
        """
        Find a guild using the Guild's name or a Player's UUID.

        Parameters
        ----------
        guild_name: t.Optional[str]
            The name of the Guild. Defaults to None.
        player_uuid: t.Optional[str]
            The UUID of the Player to find his guild. Defaults to None.

        Returns
        -------
        find_guild.FindGuild
            The ID of the guild being find.
        """
        if guild_name:
            json = await self._fetch(self.url["find_guild"], {"byName": guild_name})
        elif player_uuid:
            json = await self._fetch(self.url["find_guild"], {"byUuid": player_uuid})
        else:
            raise InvalidArgumentError(
                "Please provide a Named argument of the guild's Name or guild's ID."
            )

        return find_guild.FindGuild(json)

    async def get_player_status(
        self, name: t.Optional[str] = None, uuid: t.Optional[str] = None
    ) -> player_status.PlayerStatus:
        """
        Get the status about a Player using his username or UUID.

        Parameters
        ----------
        name: t.Optional[str]
            The Optional string value for the Username. Defaults to None.
        uuid: t.Optional[str]
            The Optional string Value to the UUID. Defaults to None.

        Returns
        -------
        player_status.PlayerStatus
            The Player status object consisting of all info from the API.
        """
        uuid = self._filter_name_uuid(name, uuid)
        json = await self._fetch(self.url["status"], {"uuid": uuid})

        return player_status.PlayerStatus(json)

    async def get_player_recent_games(
        self, name: t.Optional[str] = None, uuid: t.Optional[str] = None
    ) -> recent_games.RecentGames:
        """
        Get the recent games played by a Hypixel player using his Username or UUID.

        Parameters
        ----------
        name: t.Optional[str]
            The Optional string value for the Username. Defaults to None.
        uuid: t.Optional[str]
            The Optional string Value to the UUID. Defaults to None.

        Returns
        -------
        recent_games.RecentGames
            The recent games for the respective player specified.
        """
        uuid = self._filter_name_uuid(name, uuid)
        json = await self._fetch(self.url["recent_games"], {"uuid": uuid})

        return recent_games.RecentGames(json)

    async def get_skyblock_profile(
        self, name: t.Optional[str] = None, uuid: t.Optional[str] = None
    ) -> skyblock.SkyblockProfile:
        """
        Get the skyblock information and profile about a specific user as passed in the requirements.

        Parameters
        ----------
        name: t.Optional[str]
            The player's name in Hypixel
        uuid: t.Optional[str]
            The player's global UUID

        Returns
        -------
        skyblock.SkyblockProfile
            The skyblock profile model for the specified user.
        """
        uuid = self._filter_name_uuid(name, uuid)
        json = await self._fetch(self.url["skyblock_profile"], {"profile": uuid})

        if not json["profile"]:
            raise PlayerNotFoundError(
                "The skyblock player being searched does not exist!", uuid
            )

        return skyblock.SkyblockProfile(json)

    async def get_skyblock_user_auctions(
        self, name: t.Optional[str] = None, uuid: t.Optional[str] = None
    ) -> skyblock.SkyblockUserAuction:
        """
        Get the skyblock auction info about a specific user.

        Parameters
        ----------
        name: t.Optional[str]
            The player's name in Hypixel
        uuid: t.Optional[str]
            The player's global UUID

        Returns
        -------
        skyblock.SkyblockUserAuction
            The skyblock auction model for the user.
        """
        uuid = self._filter_name_uuid(name, uuid)
        json = await self._fetch(self.url["skyblock_auctions"], {"profile": uuid})

        if not json["auctions"]:
            raise PlayerNotFoundError(
                "The skyblock player being searched does not exist!", uuid
            )

        return skyblock.SkyblockUserAuction(json)

    async def get_skyblock_active_auctions(
        self, page: int = 0
    ) -> skyblock.SkyblockActiveAuction:
        """
        Get the list of active auctions in skyblock and use the data.

        Parameters
        ----------
        page: int
            The skyblock auction page to lookup.

        Returns
        -------
        skyblock.SkyblockActiveAuction
            The active auction model.
        """
        json = await self._fetch(self.url["skyblock_active_auctions"], {"page": page})
        return skyblock.SkyblockActiveAuction(json)

    async def get_skyblock_bazaar(self) -> skyblock.SkyblockBazaar:
        """
        Get the skyblock bazaar items

        Returns
        -------
        skyblock.SkyblockBazaar
            The bazaar model object representing each product.
        """
        json = await self._fetch(self.url["skyblock_bazaar"])
        return skyblock.SkyblockBazaar(json)

    async def get_resources_achievements(self) -> dict:
        """
        Get the current resources.

        Returns
        -------
        dict
            Hypixel API response.
        """
        data = await self._fetch(self.url["achievements"], api_key=False)
        return data["achievements"]

    async def get_resources_challenges(self) -> dict:
        """
        Get the current resources.

        Returns
        -------
        dict
            Hypixel API response.
        """
        data = await self._fetch(self.url["challenges"], api_key=False)
        return data["challenges"]

    async def get_resources_quests(self) -> dict:
        """
        Get the current resources.

        Returns
        -------
        dict
            Hypixel API response.
        """
        data = await self._fetch(self.url["quests"], api_key=False)
        return data["quests"]

    async def get_resources_guild_achievements(self) -> dict:
        """
        Get the current resources.

        Returns
        -------
        dict
            Hypixel API response.
        """
        data = await self._fetch(self.url["guild_achievements"], api_key=False)
        return {"one_time": data["one_time"], "tiered": data["tiered"]}
