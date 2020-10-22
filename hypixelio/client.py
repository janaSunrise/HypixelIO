import typing as t
import random

import requests

from .utils.helpers import (
    form_url
)

from .models import (
    boosters,
    friends,
    guild,
    key,
    player,
    watchdog,
)

from .exceptions.exceptions import (
    InvalidArgumentError,
    HypixelAPIError,
    RateLimitError,
    PlayerNotFoundError,
    GuildNotFoundError
)

# Constant Variables Definition

HYPIXEL_API = "https://api.hypixel.net"
MOJANG_API = "https://api.mojang.com"


class Client:
    """
    This Client Contains the Authentication, and Request system for the Hypixel API.

    Attributes:
        api_key (t.Union[str, list]):
            This contains the Api Key, or the List of API Keys for the authentication.
    """
    def __init__(self, api_key: t.Union[str, list]) -> None:
        """
        The constructor for the `Client` class.

        Parameters:
            api_key (str): The API Key generated in Hypixel using `/api new` command.
        """
        if not isinstance(api_key, list):
            self.api_key = [api_key]

        # Define the class variables to be used
        self.session = requests
        self.timeout = 10

    def fetch(self, url: str, data: dict = None) -> dict:
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

        with self.session.get(url, timeout=self.timeout) as response:

            if response.status_code == 429:
                raise RateLimitError("Out of Requests!")

            try:
                json = response.json()
                return json, json["success"]
            except Exception as exception:
                raise HypixelAPIError(f"Invalid Content type Receieved instead of JSON. {exception}")

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

        json, success = self.fetch("/key", {"key": api_key})

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
        json, success = self.fetch("/boosters")

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
            json, success = self.fetch("/player", {"name": name})
        elif uuid:
            json, success = self.fetch("/player", {"uuid": uuid})
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
            json, success = self.fetch("/friends", {"uuid": uuid})
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
        json, success = self.fetch("/watchdogstats")

        if not success:
            raise HypixelAPIError(
                f"The Key given is invalid, or something else has problem. Cause: {json['cause']}"
            )

        return watchdog.Watchdog(
            json
        )

    def get_guild(self, name: t.Optional[str] = None, id: t.Optional[str] = None) -> guild.Guild:
        """
        Get the Info about a Hypixel Guild, Either using Name or UUID.

        Parameters:
            name (t.Optional[str]): The Name of the Guild.
            id (t.Optional[str])L The ID Of the guild.

        Returns:
            guild (Guild): The Guild Object with certain Attributes for you to access, and use it.
        """
        if id:
            json, success = self.fetch("/guild", {"id": id})
        elif name:
            json, success = self.fetch("/guild", {"name": name})
        else:
            raise InvalidArgumentError("Please provide a Named argument of the guild's Name or guild's ID.")

        if not success:
            raise HypixelAPIError("The Key given is invalid, or something else has problem.")

        if not json["guild"]:
            raise GuildNotFoundError("Return Value is null")

        return guild.Guild(
            json["guild"]
        )
