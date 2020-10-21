import aiohttp

import typing as t
import random

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
    def __init__(self, api_key: t.Union[str, list]) -> None:
        if not isinstance(api_key, list):
            self.api_key = [api_key]

        # Define the class variables to be used
        self.session = aiohttp.ClientSession()
        self.timeout = 10

    def close(self) -> None:
        """Close the aiohttp session when you're done."""
        self.session.close()

    async def form_url(self, url: str, data: dict = {}) -> str:
        url = HYPIXEL_API + url if url.startswith('/') else url
        url += "?" + "&".join(
            [
                f"{dict_key}={dict_value}" for dict_key, dict_value in data.items()
            ]
        )

        return url

    async def fetch(self, url: str, data: dict = {}) -> dict:
        if "key" in data:
            data["key"] = key
        else:
            data["key"] = random.choice(self.api_key)

        url = self.form_url(url, data)

        async with self.session.get(url, timeout=self.timeout) as response:

            if response.status == 429:
                raise RateLimitError("Out of Requests!")

            try:
                json = await response.json()
                return json, json["success"]
            except Exception as e:
                raise HypixelAPIError(f"Invalid Content type Receieved instead of JSON. {e}")

    async def get_key(self, api_key: str = None) -> key.Key:
        api_key = None if None else random.choice(self.api_key)

        json, success = self.fetch("/key", data={'key': api_key})

        if not success:
            raise HypixelAPIError("The Key given is invalid, or something else has problem.")

        return key.Key(
            json["record"]
        )

    async def get_boosters(self) -> boosters.Boosters:
        json, success = self.fetch("/boosters")

        if not success:
            raise HypixelAPIError("The Key given is invalid, or something else has problem.")

        return boosters.Boosters(
            json["boosters"]
        )

    async def get_player(self, name: t.Optional[str] = None, uuid: t.Optional[str] = None) -> player.Player:
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
                player = name
            else:
                player = uuid
            raise PlayerNotFoundError("Null Value is returned", player)

        return player.Player(
            json["player"]
        )

    async def get_friends(self, uuid: t.Optional[str] = None) -> friends.Friend:
        if not uuid:
            raise InvalidArgumentError("Please provide a Named argument of the player's UUID")
        else:
            json, success = self.fetch("/player", {"uuid": uuid})

        if not success:
            raise HypixelAPIError("The Key given is invalid, or something else has problem.")

        return friends.Friends(
            json["records"]
        )

    async def get_watchdog_info(self) -> watchdog.Watchdog:
        json, success = self.fetch("/watchdogstats")

        if not success:
            raise HypixelAPIError(
                f"The Key given is invalid, or something else has problem. Cause: {json['cause']}"
            )

        return watchdog.Watchdog(
            json
        )

    async def get_guild(self, name: t.Optional[str] = None, id: t.Optional[str] = None) -> guild.Guild:
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

# TODO: games, leaderboard
