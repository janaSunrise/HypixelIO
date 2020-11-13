import typing as t
import random

import requests
import requests_cache

from hypixelio.utils.helpers import (
    form_url
)

from hypixelio.utils.constants import (
    HYPIXEL_API,
    TIMEOUT,
)

from hypixelio.models import (
    boosters,
    caching,
    friends,
    games,
    guild,
    key,
    leaderboard,
    player,
    watchdog,
    find_guild,
)

from hypixelio.exceptions.exceptions import (
    InvalidArgumentError,
    HypixelAPIError,
    RateLimitError,
    PlayerNotFoundError,
    GuildNotFoundError
)


class Client:
    """
    This Client Contains the Authentication, and Request system for the Hypixel API.

    Attributes:
        api_key (t.Union[str, list]):
            This contains the Api Key, or the List of API Keys for the authentication.
    """
    def __init__(self, api_key: t.Union[str, list], cache: bool = False, cache_config: caching.Caching = None) -> None:
        """
        The constructor for the `Client` class.

        Parameters:
            api_key (str): The API Key generated in Hypixel using `/api new` command.
            cache (bool): Whether to enable caching
            cache_config (Caching): The configuration for the saving, and reusing of the cache
        """
        if not isinstance(api_key, list):
            self.api_key = [api_key]

        if cache:
            requests_cache.install_cache(
                cache_name=cache_config.cache_name,
                backend=cache_config.backend,
                expire_after=cache_config.expire_after,
                old_data_on_error=cache_config.old_data_on_error,
            )

    def _fetch(self, url: str, data: dict = None) -> t.Union[dict, bool]:
        """
        Get the JSON Response from the Root Hypixel API URL,
        and Also add the ability to include the GET request parameters
        with the API KEY Parameter by default.

        Parameters:
            url (str): The URL to be accessed from the Root Domain.
            data (dict):
                The GET Request's Key-Value Pair. Example: {"uuid": "abc"} is converted to `?uuid=abc`

        Returns:
            JSON Response, Request Success (tuple):
                The JSON Response from the Fetch Done to the API and the SUCCESS Value from the Response.
        """
        if not data:
            data = {}

        if "key" not in data:
            data["key"] = random.choice(self.api_key)

        url = form_url(HYPIXEL_API, url, data)

        with requests.get(url, timeout=TIMEOUT) as response:

            if response.status_code == 429:
                raise RateLimitError("Out of Requests!")

            try:
                json = response.json()
                return json, json["success"]
            except Exception as exception:
                raise HypixelAPIError(f"Invalid Content type Received instead of JSON. {exception}")

    def get_key_info(self, api_key: t.Optional[str] = None) -> key.Key:
        """
        Get the Info about an API Key generated in Hypixel.

        Parameters:
            api_key (t.Optional[str]): The API Key generated in Hypixel using `/api new` command.

        Returns:
            key (Key): Key object for the API Key.
        """
        if not api_key:
            api_key = random.choice(self.api_key)

        json, success = self._fetch("/key", {"key": api_key})

        if not success:
            raise HypixelAPIError("The Key given is invalid, or something else has problem.")

        return key.Key(
            json["record"]
        )

    def get_boosters(self) -> boosters.Boosters:
        """
        Get the List of Hypixel Coin Boosters and Their Info.

        Parameters:
            None

        Returns:
            boosters (Boosters): The Booster Class Object, Which depicts the Booster Data Model.
        """
        json, success = self._fetch("/boosters")

        if not success:
            raise HypixelAPIError("The Key given is invalid, or something else has problem.")

        return boosters.Boosters(
            json["boosters"]
        )

    def get_player(self, name: t.Optional[str] = None, uuid: t.Optional[str] = None) -> player.Player:
        """
        Get the Info about a Hypixel Player using either his Username or UUID.

        Parameters:
            name (t.Optional[str]): The Optional string value for the Username
            uuid (t.Optional[str]): The Optional string Value to the UUID

        Returns:
            player (Player): The Player Class Object, Which depicts the Player Data Model.
        """
        if name:
            json, success = self._fetch("/player", {"name": name})
        elif uuid:
            json, success = self._fetch("/player", {"uuid": uuid})
        else:
            raise InvalidArgumentError("Please provide a Named argument of the player's username or player's UUID.")

        if not success:
            raise HypixelAPIError("The Key given is invalid, or something else has problem.")

        if not json["player"]:
            if name:
                player_model = name
            else:
                player_model = uuid
            raise PlayerNotFoundError("Null Value is returned", player_model)

        return player.Player(
            json["player"]
        )

    def get_friends(self, uuid: t.Optional[str] = None) -> friends.Friends:
        """
        Get the List of Friends of a Hypixel Player and their Info.

        Parameters:
            uuid (t.Optional[str]): The UUID of a Certain Hypixel Player.

        Returns:
            friends (Friends):
                Returns the Friend Data Model, Which has the List of Friends, Each with a List of Attributes.
        """
        if uuid:
            json, success = self._fetch("/friends", {"uuid": uuid})
        else:
            raise InvalidArgumentError("Please provide a Named argument of the player's UUID")

        if not success:
            raise HypixelAPIError("The Key given is invalid, or something else has problem.")

        return friends.Friends(
            json["records"]
        )

    def get_watchdog_info(self) -> watchdog.Watchdog:
        """
        Get the List of Stats About the Watchdog for the last few days.

        Parameters:
            None

        Returns:
            watchdog (Watchdog):
                The Watchdog data model with certain important attributes for you to get data about the things by watchdog.
        """
        json, success = self._fetch("/watchdogstats")

        if not success:
            raise HypixelAPIError(
                f"The Key given is invalid, or something else has problem. Cause: {json['cause']}"
            )

        return watchdog.Watchdog(
            json
        )

    def get_guild(self, name: t.Optional[str] = None, uuid: t.Optional[str] = None) -> guild.Guild:
        """
        Get the Info about a Hypixel Guild, Either using Name or UUID.

        Parameters:
            name (t.Optional[str]): The Name of the Guild.
            uuid (t.Optional[str]): The ID Of the guild.

        Returns:
            guild (Guild): The Guild Object with certain Attributes for you to access, and use it.
        """
        if uuid:
            json, success = self._fetch("/guild", {"id": uuid})
        elif name:
            json, success = self._fetch("/guild", {"name": name})
        else:
            raise InvalidArgumentError("Please provide a Named argument of the guild's Name or guild's ID.")

        if not success:
            raise HypixelAPIError("The Key given is invalid, or something else has problem.")

        if not json["guild"]:
            raise GuildNotFoundError("Return Value is null")

        return guild.Guild(
            json["guild"]
        )

    def get_games_info(self) -> games.Games:
        """
        Get the List of Hypixel Games and Their Info.

        Parameters:
            None

        Returns:
            games (Games): The Games Data model, Containing the information, and attributes for all the games.
        """
        json, success = self._fetch("/gameCounts")

        if not success:
            raise HypixelAPIError("The Key given is invalid, or something else has problem.")

        return games.Games(
            json["games"],
            json["playerCount"]
        )

    def get_leaderboards(self) -> leaderboard.Leaderboard:
        """
        Get the Leaderboard for all the games, along with the data in it.

        Parameters:
            None

        Returns:
            leaderboard (Leaderboard): The Leaderboard data model, containing all the ranking for the games in Hypixel.
        """
        json, success = self._fetch("/leaderboards")

        if not success:
            raise HypixelAPIError("The Key given is invalid, or something else has problem.")

        return leaderboard.Leaderboard(
            json["leaderboards"]
        )

    def find_guild(self, guild_name: t.Optional[str] = None, player_uuid: t.Optional[str] = None) -> find_guild.FindGuild:
        """
        Finds the Guild By the Guild's Name or using a Player's UUID

        Parameters:
            guild_name (t.Optional[str]) : The name of the Guild
            player_uuid (t.Optional[str]): The UUID of the Player to find his guild.

        Returns:
            guild_id (FindGuild): The ID of the guild being find.
        """
        if guild_name:
            json, success = self._fetch("/findGuild", {"byName": guild_name})
        elif player_uuid:
            json, success = self._fetch("/findGuild", {"byUuid": player_uuid})
        else:
            raise InvalidArgumentError("Please provide a Named argument of the guild's Name or guild's ID.")

        if not success:
            raise HypixelAPIError("The Key given is invalid, or something else has problem.")
        
        return find_guild.FindGuild(
            json
        )
