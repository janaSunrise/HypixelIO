__all__ = (
    "Utils",
    "get_guild_display",
    "get_guild_level",
    "get_guild_level_exact",
    "get_increase",
    "get_level_percentage",
    "get_network_level",
    "get_network_level_exact",
    "get_profile_display",
    "get_rank",
    "get_rank_color",
    "get_ratio",
    "get_ratio_next",
    "get_skywars_level",
    "get_skywars_level_exact"
)

import math
import re
import typing as t

import requests
from requests.models import Response

from hypixelio.endpoints import API_PATH
from hypixelio.exceptions.exceptions import (
    CrafatarAPIError,
    InvalidArgumentError,
)
from hypixelio.lib.converters import (
    Converters
)
from hypixelio.utils.constants import (
    RANKS,
    RANK_COLORS,
    TIMEOUT
)


class Utils:
    mojang_url = API_PATH["MOJANG"]
    url = API_PATH["CRAFATAR"]

    @classmethod
    def _crafatar_fetch(cls, url: str) -> Response:
        """
        This is the function for fetching the JSON from the Crafatar API.

        Parameters
        ----------
        url: `str`
            The Crafatar URL, whose JSON is supposed to be fetched.

        Returns
        -------
        `t.Optional[dict]`
            The JSON response from the Crafatar API, which is returned.
        """
        with requests.get(f"https://crafatar.com/{url}", timeout=TIMEOUT) as response:
            if response.status_code == 422:
                raise InvalidArgumentError("Invalid data passed for conversion!")

            try:
                return response
            except Exception:
                raise CrafatarAPIError("There seems to be some problem with the content type or the API IS down.")

    @staticmethod
    def _filter_name_uuid(name: t.Optional[str] = None, uuid: t.Optional[str] = None) -> str:
        if not name and not uuid:
            raise InvalidArgumentError("Please provide a named argument of the player's username or player's UUID.")

        if name:
            uuid = Converters.username_to_uuid(name)

        return uuid

    @classmethod
    def _form_crafatar_url(cls, route: str) -> str:
        """
        This function forms the crafatar API URL for fetching USER skins.

        Parameters
        ----------
        route: `str`
            The URL path to visit.

        Returns
        -------
        `str`
            The well formed API URL for fetching.
        """
        return f"https://crafatar.com{route}"

    @classmethod
    def get_name_history(
            cls, name: t.Optional[str] = None, uuid: t.Optional[str] = None, changed_at: bool = False
    ) -> t.Union[list, dict]:
        """
        This get the name history with records of a player.

        Parameters
        ----------
        name: `t.Optional[str]`
            The username of the player. Defaults to None.
        uuid: `t.Optional[str]`
            The UUID of the player. Defaults to None.
        changed_at: `bool`
            Toggle to true, if you need when the player changed name. Defaults to False.

        Returns
        -------
        `t.Union[list, dict]`
            The list or dictionary with the name history and records.
        """
        uuid = cls._filter_name_uuid(name, uuid)
        json = Converters._fetch(Utils.mojang_url["name_history"].format(uuid))

        if changed_at:
            return json

        usernames = []
        for data in json:
            usernames.append(data["name"])

        return usernames

    @classmethod
    def get_avatar(cls, name: t.Optional[str] = None, uuid: t.Optional[str] = None) -> str:
        """
        Get the avatar of the specified player

        Parameters
        ----------
        name: `t.Optional[str]`
            The username of the player. Defaults to None.
        uuid: `t.Optional[str]`
            The UUID of the player. Defaults to None.

        Returns
        -------
        `str`
            The URL containing the image of the avatar.
        """
        uuid = cls._filter_name_uuid(name, uuid)
        Utils._crafatar_fetch(Utils.url["avatar"].format(uuid))

        return Utils._form_crafatar_url(Utils.url["avatar"].format(uuid))

    @classmethod
    def get_head(cls, name: t.Optional[str] = None, uuid: t.Optional[str] = None) -> str:
        """
        Get the head skin of the specified player

        Parameters
        ----------
        name: `t.Optional[str]`
            The username of the player. Defaults to None.
        uuid: `t.Optional[str]`
            The UUID of the player. Defaults to None.

        Returns
        -------
        `str`
            The URL containing the image of the head.
        """
        uuid = cls._filter_name_uuid(name, uuid)
        Utils._crafatar_fetch(Utils.url["head"].format(uuid))

        return Utils._form_crafatar_url(Utils.url["head"].format(uuid))

    @classmethod
    def get_body(cls, name: t.Optional[str] = None, uuid: t.Optional[str] = None) -> str:
        """
        Get the whole body's skin of the specified player

        Parameters
        ----------
        name: `t.Optional[str]`
            The username of the player. Defaults to None.
        uuid: `t.Optional[str]`
            The UUID of the player. Defaults to None.

        Returns
        -------
        `str`
            The URL containing the image of the whole body.
        """
        uuid = cls._filter_name_uuid(name, uuid)
        Utils._crafatar_fetch(Utils.url["body"].format(uuid))

        return Utils._form_crafatar_url(Utils.url["body"].format(uuid))


def get_ratio(positive_stat: t.Union[int, float], negative_stat: t.Union[int, float]) -> t.Union[int, float]:
    try:
        ratio = positive_stat / negative_stat
        return round(ratio, 2)
    except ZeroDivisionError:
        return float("inf") if positive_stat > 0 else 0


def get_ratio_next(ratio: t.Union[int, float]) -> t.Union[int, float]:
    if ratio == float("inf"):
        return ratio
    return math.trunc(ratio) + 1


def get_increase(positive_stat: t.Union[int, float], negative_stat: t.Union[int, float], *, amount: int = 0) -> t.Any:
    ratio = get_ratio(positive_stat, negative_stat)
    if ratio == float("inf"):
        return 0
    if not bool(amount):
        amount = (math.trunc(ratio) + 1) - ratio
    needed = (ratio + amount) * negative_stat - positive_stat
    return round(needed)


def get_level_percentage(level: float) -> t.Union[int, float]:
    return round((level - math.trunc(level)) * 100, 2)


def get_network_level(experience: t.Union[int, float]) -> t.Union[int, float]:
    return math.trunc(get_network_level_exact(experience))


def get_network_level_exact(experience: t.Union[int, float]) -> t.Union[int, float]:
    return (math.sqrt(experience + 15312.5) - 88.38834764831843) / 35.35533905932738


def get_skywars_level(experience: t.Union[int, float]) -> t.Union[int, float]:
    return math.trunc(get_skywars_level_exact(experience))


def get_skywars_level_exact(experience: t.Union[int, float]) -> t.Union[int, float]:
    total_xp = [20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
    level = 0

    if experience >= 15000:
        level = (experience - 15000) / 10000 + 12
    else:
        counter = 0
        while experience >= 0 and counter < len(total_xp):
            if experience - total_xp[counter] >= 0:
                counter += 1
            else:
                level = counter + 1 + (experience - total_xp[counter - 1]) / (total_xp[counter] - total_xp[counter - 1])
                break
    return level


def get_rank(rank: str, prefix_raw: str, monthly_package_rank: str, new_package_rank: str, package_rank: str) -> None:
    real_rank = None

    if prefix_raw:
        prefix = re.sub(r"§.", "", prefix_raw)[1:-1]
        real_rank = RANKS.get(prefix, prefix)
    elif rank and rank != "NORMAL" and not real_rank:
        real_rank = RANKS.get(rank, rank)
    elif new_package_rank and not real_rank:
        real_rank = RANKS.get(new_package_rank, new_package_rank)
    elif package_rank and not real_rank:
        real_rank = RANKS.get(package_rank, package_rank)
    elif (monthly_package_rank and monthly_package_rank != "NONE") and not real_rank:
        real_rank = RANKS.get(monthly_package_rank, monthly_package_rank)

    return real_rank


def get_rank_color(rank: str) -> str:
    return RANK_COLORS[rank]


def get_profile_display(name: str, rank: str) -> str:
    if bool(rank):
        return f"[{rank}] {name}"
    return name


def get_guild_level(experience: t.Union[int, float]) -> t.Union[int, float]:
    return math.trunc(get_guild_level_exact(experience))


def get_guild_level_exact(experience: int) -> t.Union[float, int]:
    experience_below_14 = [
        100000,
        150000,
        250000,
        500000,
        750000,
        1000000,
        1250000,
        1500000,
        2000000,
        2500000,
        2500000,
        2500000,
        2500000,
        2500000
    ]
    c = 0.0
    for it in experience_below_14:
        if it > experience:
            level = c + round(experience / it * 100.0) / 100.0
        experience -= it
        c += 1

        increment = 3000000
    while experience > increment:
        c += 1
        experience -= increment
    level = c + (round(experience / increment * 100.0) / 100.0)
    return level


def get_guild_display(name: str, tag: str) -> str:
    if tag:
        return f"[{tag}] {name}"
    return name
