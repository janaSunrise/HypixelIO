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

        >>> from hypixelio.ext.asyncio import AsyncClient

    If you have a single API key, Here's how to authenticate

        >>> client = AsyncClient(api_key="123-456-789")

    Or, If you have multiple API keys (Better option for load balancing)

        >>> client = AsyncClient(api_key=["123-456", "789-000", "568-908"])

    if you want to enable caching, Here's how to do it
        >>> client = AsyncClient(cache=True)

    And configuring cache
        >>> from hypixelio.models.caching import Caching, CacheBackend
        >>> cache_cfg = Caching(cache_name="my-cache", backend=CacheBackend.sqlite, expire_after=10)
        >>> client = AsyncClient(cache=True, cache_config=cache_cfg)

    You can also manipulate the cache object by accessing using
        >>> client.cache
    And call methods as needed.

    Notes
    -----
    Keep in mind that, your keys wouldn't work if you're banned from hypixel, or if they're expired.
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
        api_key: `t.Union[str, list]`
            The API Key generated in Hypixel using `/api new` command.
        cache: `t.Optional[bool]`
            Whether to enable caching
        cache_config: `t.Optional[caching.Caching]`
            The configuration for the saving, and reusing of the cache. Defaults to None.
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
        Get the JSON Response from the Root Hypixel API URL, and also add the ability to include the GET request
        parameters with the API KEY Parameter by default.

        Parameters
        ----------
        url: `str`
            The URL to be accessed from the Root Domain.
        data: `t.Optional[dict]`
            The GET Request's Key-Value Pair. Example: {"uuid": "abc"} is converted to `?uuid=abc`. Defaults to None.

        Returns
        -------
        `t.Tuple[dict, bool]`
            The JSON Response from the Fetch Done to the API and the SUCCESS Value from the Response.
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
                # 429 status code handling
                if response.status == 429:
                    self._handle_ratelimit(response.headers)

                # 400 Status code handling
                if response.status == 400:
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
        Get the Info about an API Key generated in Hypixel.

        Parameters
        ----------
        api_key: `t.Optional[str]`
            The API Key generated in Hypixel using `/api new` command. Defaults to None.

        Returns
        -------
        `key.Key`
            Key object for the API Key.
        """
        if not api_key:
            api_key = random.choice(self._api_key)

        json = await self._fetch(self.url["api_key"], {"key": api_key})
        return key.Key(json["record"])

    async def get_boosters(self) -> boosters.Boosters:
        """
        Get the List of Hypixel Coin Boosters and Their Info.

        Returns
        -------
        `boosters.Boosters`
            The Booster class object which depicts the booster data model.
        """
        json = await self._fetch(self.url["boosters"])

        return boosters.Boosters(json["boosters"], json)

    async def get_player(
        self, name: t.Optional[str] = None, uuid: t.Optional[str] = None
    ) -> player.Player:
        """
        Get the Info about a Hypixel Player using either his Username or UUID.

        Parameters
        ----------
        name: `t.Optional[str]`
            The Optional string value for the Username. Defaults to None.
        uuid: `t.Optional[str]`
            The Optional string Value to the UUID. Defaults to None.

        Returns
        -------
        `player.Player`
            The Player Class Object, Which depicts the Player Data Model
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
        Get the List of Friends of a Hypixel Player and their Info.

        Parameters
        ----------
        name: `t.Optional[str]`
            The Optional string value for the Username of a hypixel player.. Defaults to None.
        uuid: `t.Optional[str]`
            The UUID of a Certain Hypixel Player. Defaults to None.

        Returns
        -------
        `friends.Friends`
            Returns the Friend Data Model, Which has the List of Friends, each with a list of attributes.
        """
        uuid = self._filter_name_uuid(name, uuid)
        json = await self._fetch(self.url["friends"], {"uuid": uuid})

        return friends.Friends(json["records"])

    async def get_watchdog_info(self) -> watchdog.Watchdog:
        """
        Get the List of Stats About the Watchdog for the last few days.

        Returns
        -------
        `watchdog.Watchdog`
            The Watchdog data model with certain important attributes for you to get data about the things by watchdog.
        """
        json = await self._fetch(self.url["watchdog"])

        return watchdog.Watchdog(json)

    async def get_guild(
        self, name: t.Optional[str] = None, uuid: t.Optional[str] = None
    ) -> guild.Guild:
        """
        Get the info about a Hypixel Guild, Either using Name or UUID.

        Parameters
        ----------
        name: `t.Optional[str]`
            The Name of the Guild. Defaults to None.
        uuid: `t.Optional[str]`
            The ID Of the guild. Defaults to None.

        Returns
        -------
        `guild.Guild`
            The Guild Object with certain Attributes for you to access, and use it.
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
        Get the List of Hypixel Games and Their Info.

        Returns
        -------
        `games.Games`
            The Games Data model, Containing the information, and attributes for all the games.
        """
        json = await self._fetch(self.url["game_info"])

        return games.Games(json["games"], json["playerCount"])

    async def get_leaderboards(self) -> leaderboard.Leaderboard:
        """
        Get the Leaderboard for all the games, along with the data in it.

        Returns
        -------
        `leaderboard.Leaderboard`
            The Leaderboard data model, containing all the ranking for the games in Hypixel.
        """
        json = await self._fetch(self.url["leaderboards"])

        return leaderboard.Leaderboard(json["leaderboards"])

    async def find_guild(
        self, guild_name: t.Optional[str] = None, player_uuid: t.Optional[str] = None
    ) -> find_guild.FindGuild:
        """
        Finds the Guild By the Guild's Name or using a Player's UUID

        Parameters
        ----------
        guild_name: `t.Optional[str]`
            The name of the Guild. Defaults to None.
        player_uuid: `t.Optional[str]`
            The UUID of the Player to find his guild. Defaults to None.

        Returns
        -------
        `find_guild.FindGuild`
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
        Get the Status info about a Hypixel Player using either his Username or UUID.

        Parameters
        ----------
        name: `t.Optional[str]`
            The Optional string value for the Username. Defaults to None.
        uuid: `t.Optional[str]`
            The Optional string Value to the UUID. Defaults to None.

        Returns
        -------
        `player_status.PlayerStatus`
            The Player Status Object, which depicts the Player's status
        """
        uuid = self._filter_name_uuid(name, uuid)
        json = await self._fetch(self.url["status"], {"uuid": uuid})

        return player_status.PlayerStatus(json)

    async def get_player_recent_games(
        self, name: t.Optional[str] = None, uuid: t.Optional[str] = None
    ) -> recent_games.RecentGames:
        """
        Get the recent games played by a Hypixel Player using either his Username or UUID.

        Parameters
        ----------
        name: `t.Optional[str]`
            The Optional string value for the Username. Defaults to None.
        uuid: `t.Optional[str]`
            The Optional string Value to the UUID. Defaults to None.

        Returns
        -------
        `recent_games.RecentGames`
            The recent games model for the respective player specified.
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
        name: `str`
            The player's name in Hypixel
        uuid: `str`
            The player's global UUID

        Returns
        -------
        `skyblock.SkyblockProfile`
            The skyblock profile model for the user.
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
        Get the skyblock auction info about a specific user as passed in the requirements.

        Parameters
        ----------
        name: `str`
            The player's name in Hypixel
        uuid: `str`
            The player's global UUID

        Returns
        -------
        `skyblock.SkyblockUserAuction`
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