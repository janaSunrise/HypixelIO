__all__ = "Utils"

import typing as t

import aiohttp

from hypixelio.endpoints import API_PATH
from hypixelio.exceptions.exceptions import (
    CrafatarAPIError,
    InvalidArgumentError,
)
from hypixelio.ext.asyncio.converters import (
    AsyncConverters as Converters
)
from hypixelio.utils.constants import (
    TIMEOUT
)


class Utils:
    mojang_url = API_PATH["MOJANG"]
    url = API_PATH["CRAFATAR"]

    @classmethod
    async def _crafatar_fetch(cls, url: str) -> t.Any:
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
        session = aiohttp.ClientSession()

        async with session.get(f"https://crafatar.com/{url}", timeout=TIMEOUT) as response:
            if response.status == 422:
                raise InvalidArgumentError("Invalid data passed for conversion!")

            try:
                return await response.text()
            except Exception:
                raise CrafatarAPIError("There seems to be some problem with the content type or the API IS down.")

        await session.close()

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
    async def get_name_history(
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
        json = await Converters._fetch(Utils.mojang_url["name_history"].format(uuid))

        if changed_at:
            return json

        usernames = []
        for data in json:
            usernames.append(data["name"])

        return usernames

    @classmethod
    async def get_avatar(cls, name: t.Optional[str] = None, uuid: t.Optional[str] = None) -> str:
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
        await Utils._crafatar_fetch(Utils.url["avatar"].format(uuid))

        return Utils._form_crafatar_url(Utils.url["avatar"].format(uuid))

    @classmethod
    async def get_head(cls, name: t.Optional[str] = None, uuid: t.Optional[str] = None) -> str:
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
        await Utils._crafatar_fetch(Utils.url["head"].format(uuid))

        return Utils._form_crafatar_url(Utils.url["head"].format(uuid))

    @classmethod
    async def get_body(cls, name: t.Optional[str] = None, uuid: t.Optional[str] = None) -> str:
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
        await Utils._crafatar_fetch(Utils.url["body"].format(uuid))

        return Utils._form_crafatar_url(Utils.url["body"].format(uuid))
