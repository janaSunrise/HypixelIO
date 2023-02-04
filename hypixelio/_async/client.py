__all__ = ("AsyncClient",)

import asyncio
import random
from types import TracebackType
from typing import (
    Any,
    Dict,
    Optional,
    Type,
    Union,
    cast
)

import aiohttp

from .converters import AsyncConverters
from ..base import BaseClient
from ..constants import HYPIXEL_API, TIMEOUT
from ..exceptions import (
    GuildNotFoundError,
    HypixelAPIError,
    InvalidArgumentError,
    PlayerNotFoundError,
    RateLimitError,
)
from ..models.boosters import Boosters
from ..models.find_guild import FindGuild
from ..models.friends import Friends
from ..models.games import Games
from ..models.guild import Guild
from ..models.key import Key
from ..models.leaderboard import Leaderboard
from ..models.player import Player
from ..models.player_status import PlayerStatus
from ..models.recent_games import RecentGames
from ..models.skyblock import (
    SkyblockActiveAuction,
    SkyblockBazaar,
    SkyblockNews,
    SkyblockProfile,
    SkyblockUserAuction,
)
from ..models.watchdog import Watchdog
from ..utils import form_url


class AsyncClient(BaseClient):
    """
    The client for this wrapper that handles the requests, authentication, loading and usages of the end user.

    Examples
    --------
    Import the async client first.

        >>> from hypixelio._async import AsyncClient

    If you have a single API key, Here's how to authenticate

        >>> client = AsyncClient(api_key="123-456-789")

    You can use multiple API keys to authenticate too. (Better option for load balancing)

        >>> client = AsyncClient(api_key=["123-456", "789-000", "568-908"])
    """

    def __init__(self, api_key: Union[str, list]) -> None:
        """
        Parameters
        ----------
        api_key: Union[str, list]
            The API key generated in Hypixel server using the `/api new` command.
        """
        super().__init__(api_key)

        self._session: Optional[aiohttp.ClientSession] = None
        self._lock = asyncio.Lock()

    async def close(self) -> None:
        """Close the AIOHTTP sessions to prevent memory leaks."""
        if self._session is not None:
            await self._session.close()

    async def _fetch(
        self,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        api_key: bool = True,
    ) -> dict:
        """
        Fetch the JSON response from the API along with the ability to include GET request parameters and support
        Authentication using API key too.

        Parameters
        ----------
        url: str
            The URL to be accessed from the API root URL.
        data: Optional[dict]
            The GET Request's Key-Value Pair. Example: {"uuid": "abc"} is converted to `?uuid=abc`. Defaults to None.
        api_key: bool
            If key is needed for the endpoin

        Returns
        -------
        Tuple[dict, bool]
            The JSON response obtained after fetching the API, along with success value in the response.
        """
        if not self._session:
            self._session = aiohttp.ClientSession()

        # Check if ratelimit is hit
        if self._is_ratelimit_hit():
            raise RateLimitError(self.retry_after)

        if not data:
            data = {}

        # Assign a random key
        if api_key:
            self.headers["API-Key"] = random.choice(self._api_key)

        url = form_url(HYPIXEL_API, url, data)

        async with self._lock:
            async with self._session.get(
                url, headers=self.headers, timeout=TIMEOUT
            ) as response:
                # 404 handling
                if response.status == 429:
                    raise HypixelAPIError("The route specified does not exis")

                # 429 status code handling
                if response.status == 429:
                    self._handle_ratelimit(cast(dict, response.headers))

                # 403 Status code handling
                if response.status == 403:
                    raise HypixelAPIError("Invalid key specified!")

                if api_key and "RateLimit-Limit" in response.headers:
                    self._update_ratelimit(cast(dict, response.headers))

                try:
                    json = await response.json()
                except Exception as exception:
                    raise HypixelAPIError(f"{exception}")
                else:
                    if not json["success"]:
                        self._handle_api_failure(json)

                    return json

    @staticmethod
    async def _filter_name_uuid(name: Optional[str] = None, uuid: Optional[str] = None) -> str:
        if not name and not uuid:
            raise InvalidArgumentError(
                "Named argument for player's either username or UUID not found."
            )

        if name:
            uuid = await AsyncConverters.username_to_uuid(name)

        return uuid  # type: ignore

    # Context managers
    async def __aenter__(self) -> "AsyncClient":
        # Initialize the session
        self._session = aiohttp.ClientSession()

        await self._session.__aenter__()

        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        if self._session is not None:
            await self._session.__aexit__(exc_type, exc_val, exc_tb)

    # Hypixel API endpoint methods
    async def get_key_info(self, api_key: Optional[str] = None) -> Key:
        """
        Get info about a specific Hypixel API key.

        Parameters
        ----------
        api_key: Optional[str]
            The API key generated in Hypixel server using the `/api new` command. Defaults to pre-specified keys.

        Returns
        -------
        Key
            The Key object created for the API key specified.
        """
        if not api_key:
            api_key = random.choice(self._api_key)

        json = await self._fetch(self.url["api_key"], {"key": api_key})
        return Key(json["record"])

    async def get_boosters(self) -> Boosters:
        """
        Get the Hypixel coin boosters, and all the info about them.

        Returns
        -------
        Boosters
            The boosters object, with all the info from the API.
        """
        json = await self._fetch(self.url["boosters"])

        return Boosters(json["boosters"], json)

    async def get_player(
        self, name: Optional[str] = None, uuid: Optional[str] = None
    ) -> Player:
        """
        Get all info about a Hypixel player using his username or his player UUID.

        Parameters
        ----------
        name: Optional[str]
            The Optional string value for the Username. Defaults to None.
        uuid: Optional[str]
            The Optional string Value to the UUID. Defaults to None.

        Returns
        -------
        Player
            The player object with all the info obtained from the API.
        """
        uuid = await self._filter_name_uuid(name, uuid)
        json = await self._fetch(self.url["player"], {"uuid": uuid})

        if not json["player"]:
            raise PlayerNotFoundError("Null is returned", name)

        return Player(json["player"])

    async def get_friends(
        self, name: Optional[str] = None, uuid: Optional[str] = None
    ) -> Friends:
        """
        Get the friends, and all their info of specified Hypixel player.

        Parameters
        ----------
        name: Optional[str]
            The Optional string value for the Username of a hypixel player. Defaults to None.
        uuid: Optional[str]
            The UUID of a Certain Hypixel Player. Defaults to None.

        Returns
        -------
        Friends
            The Friend object with all info from the API.
        """
        uuid = await self._filter_name_uuid(name, uuid)
        json = await self._fetch(self.url["friends"], {"uuid": uuid})

        return Friends(json["records"])

    async def get_watchdog_info(self) -> Watchdog:
        """
        Get all the stats about the Watchdog (Punishment stats) for the last few days/

        Returns
        -------
        Watchdog
            The Watchdog object with all the info.
        """
        json = await self._fetch(self.url["watchdog"])

        return Watchdog(json)

    async def get_guild(
        self, name: Optional[str] = None, uuid: Optional[str] = None
    ) -> Guild:
        """
        Get info about a specific Hypixel guild using the Name, or the Guild's UUID.

        Parameters
        ----------
        name: Optional[str]
            The Name of the Guild. Defaults to None.
        uuid: Optional[str]
            The ID Of the guild. Defaults to None.

        Returns
        -------
        Guild
            The Guild object with the info fetched from the API.
        """
        if uuid:
            json = await self._fetch(self.url["guild"], {"id": uuid})
        elif name:
            json = await self._fetch(self.url["guild"], {"name": name})
        else:
            raise InvalidArgumentError(
                "Named argument for guild's name or UUID not found."
            )

        if not json["guild"]:
            raise GuildNotFoundError("Value returned is null")

        return Guild(json["guild"])

    async def get_games_info(self) -> Games:
        """
        Get the list of all Hypixel games, and their info.

        Returns
        -------
        Games
            The Games object with all the info.
        """
        json = await self._fetch(self.url["game_info"])

        return Games(json["games"], json["playerCount"])

    async def get_leaderboards(self) -> Leaderboard:
        """
        Get the leaderboard for the Hypixel games with their info.

        Returns
        -------
        Leaderboard
            The Leaderboard object with all info.
        """
        json = await self._fetch(self.url["leaderboards"])

        return Leaderboard(json["leaderboards"])

    async def find_guild(
        self, guild_name: Optional[str] = None, player_uuid: Optional[str] = None
    ) -> FindGuild:
        """
        Find a guild using the Guild's name or a Player's UUID.

        Parameters
        ----------
        guild_name: Optional[str]
            The name of the Guild. Defaults to None.
        player_uuid: Optional[str]
            The UUID of the Player to find his guild. Defaults to None.

        Returns
        -------
        FindGuild
            The ID of the guild being find.
        """
        if guild_name:
            json = await self._fetch(self.url["find_guild"], {"byName": guild_name})
        elif player_uuid:
            json = await self._fetch(self.url["find_guild"], {"byUuid": player_uuid})
        else:
            raise InvalidArgumentError(
                "Named argument for guild's name or UUID not found."
            )

        return FindGuild(json)

    async def get_player_status(
        self, name: Optional[str] = None, uuid: Optional[str] = None
    ) -> PlayerStatus:
        """
        Get the status about a Player using his username or UUID.

        Parameters
        ----------
        name: Optional[str]
            The Optional string value for the Username. Defaults to None.
        uuid: Optional[str]
            The Optional string Value to the UUID. Defaults to None.

        Returns
        -------
        PlayerStatus
            The Player status object consisting of all info from the API.
        """
        uuid = await self._filter_name_uuid(name, uuid)
        json = await self._fetch(self.url["status"], {"uuid": uuid})

        return PlayerStatus(json)

    async def get_player_recent_games(
        self, name: Optional[str] = None, uuid: Optional[str] = None
    ) -> RecentGames:
        """
        Get the recent games played by a Hypixel player using his Username or UUID.

        Parameters
        ----------
        name: Optional[str]
            The Optional string value for the Username. Defaults to None.
        uuid: Optional[str]
            The Optional string Value to the UUID. Defaults to None.

        Returns
        -------
        RecentGames
            The recent games for the respective player specified.
        """
        uuid = await self._filter_name_uuid(name, uuid)
        json = await self._fetch(self.url["recent_games"], {"uuid": uuid})

        return RecentGames(json)

    async def get_skyblock_news(self) -> SkyblockNews:
        json = await self._fetch(self.url["skyblock_news"])

        return SkyblockNews(json)

    async def get_skyblock_profile(
        self, name: Optional[str] = None, uuid: Optional[str] = None
    ) -> SkyblockProfile:
        """
        Get the skyblock information and profile about a specific user as passed in the requirements.

        Parameters
        ----------
        name: Optional[str]
            The player's name in Hypixel
        uuid: Optional[str]
            The player's global UUID

        Returns
        -------
        SkyblockProfile
            The skyblock profile model for the specified user.
        """
        uuid = await self._filter_name_uuid(name, uuid)
        json = await self._fetch(self.url["skyblock_profile"], {"profile": uuid})

        if not json["profile"]:
            raise PlayerNotFoundError("The skyblock player does not exist", uuid)

        return SkyblockProfile(json)

    async def get_skyblock_user_auctions(
        self, name: Optional[str] = None, uuid: Optional[str] = None
    ) -> SkyblockUserAuction:
        """
        Get the skyblock auction info about a specific user.

        Parameters
        ----------
        name: Optional[str]
            The player's name in Hypixel
        uuid: Optional[str]
            The player's global UUID

        Returns
        -------
        SkyblockUserAuction
            The skyblock auction model for the user.
        """
        uuid = await self._filter_name_uuid(name, uuid)
        json = await self._fetch(self.url["skyblock_auctions"], {"profile": uuid})

        if not json["auctions"]:
            raise PlayerNotFoundError("The skyblock player does not exist!", uuid)

        return SkyblockUserAuction(json)

    async def get_skyblock_active_auctions(
        self, page: int = 0
    ) -> SkyblockActiveAuction:
        """
        Get the list of active auctions in skyblock and use the data.

        Parameters
        ----------
        page: int
            The skyblock auction page to lookup.

        Returns
        -------
        SkyblockActiveAuction
            The active auction model.
        """
        json = await self._fetch(self.url["skyblock_active_auctions"], {"page": page})
        return SkyblockActiveAuction(json)

    async def get_skyblock_bazaar(self) -> SkyblockBazaar:
        """
        Get the skyblock bazaar items

        Returns
        -------
        SkyblockBazaar
            The bazaar model object representing each produc
        """
        json = await self._fetch(self.url["skyblock_bazaar"])
        return SkyblockBazaar(json)

    async def get_resources_achievements(self) -> dict:
        data = await self._fetch(self.url["achievements"], api_key=False)
        return data["achievements"]

    async def get_resources_challenges(self) -> dict:
        data = await self._fetch(self.url["challenges"], api_key=False)
        return data["challenges"]

    async def get_resources_quests(self) -> dict:
        data = await self._fetch(self.url["quests"], api_key=False)
        return data["quests"]

    async def get_resources_guild_achievements(self) -> dict:
        data = await self._fetch(self.url["guild_achievements"], api_key=False)
        return {"one_time": data["one_time"], "tiered": data["tiered"]}

    async def get_skyblock_skills(self) -> dict:
        data = await self._fetch(self.url["skyblock_skills"], api_key=False)
        return {
            "skills": data["skills"],
            "collections": data["collections"],
        }

    async def get_skyblock_collections(self) -> dict:
        data = await self._fetch(self.url["skyblock_collections"], api_key=False)
        return data["collections"]
