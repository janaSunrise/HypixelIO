__all__ = ("Utils",)

import typing as t

import aiohttp

from ..endpoints import API_PATH
from ..exceptions.exceptions import CrafatarAPIError, InvalidArgumentError
from ..utils.constants import TIMEOUT
from .converters import AsyncConverters as Converters


class Utils:
    mojang_url = API_PATH["MOJANG"]
    url = API_PATH["CRAFATAR"]

    @classmethod
    async def _crafatar_fetch(cls, url: str) -> str:
        """
        Method to fetch the JSON from the Crafatar API.

        Parameters
        ----------
        url: str
            The Crafatar URL, whose JSON is supposed to be fetched.

        Returns
        -------
        ClientResponse
            The JSON response from the Crafatar API.
        """
        session = aiohttp.ClientSession()

        async with session.get(
            f"https://crafatar.com/{url}", timeout=TIMEOUT
        ) as response:
            if response.status == 422:
                raise InvalidArgumentError(
                    "Invalid URL passed. Either user does not exist, or URL is malformed."
                )

            try:
                return await response.text()
            except Exception as exc:
                raise CrafatarAPIError() from exc

    @staticmethod
    async def _filter_name_uuid(
        name: t.Optional[str] = None,
        uuid: t.Optional[str] = None,
    ) -> str:
        if name is not None:
            return await Converters.username_to_uuid(name)
        if uuid is not None:
            return uuid
        raise InvalidArgumentError(
            "Please provide a named argument of the player's username or player's UUID."
        )

    @classmethod
    def _form_crafatar_url(cls, route: str) -> str:
        """
        This function forms the crafatar API URL for fetching skins of users.

        Parameters
        ----------
        route: str
            The URL path to form for crafatar API.

        Returns
        -------
        str
            The API URL formed to fetch.
        """
        return f"https://crafatar.com{route}"

    @classmethod
    async def get_name_history(
        cls,
        name: t.Optional[str] = None,
        uuid: t.Optional[str] = None,
        changed_at: bool = False,
    ) -> t.Union[t.List[str], t.Dict[str, t.Any]]:
        """
        Get the name history with records for a player.

        Parameters
        ----------
        name: t.Optional[str]
            The username of the player. Defaults to None.
        uuid: t.Optional[str]
            The UUID of the player. Defaults to None.
        changed_at: bool
            Toggle to true, if you need when the player changed name. Defaults to False.

        Returns
        -------
        t.Union[list, dict]
            The list or dictionary with the name history and records.
        """
        uuid = await cls._filter_name_uuid(name, uuid)
        json = await Converters._fetch(Utils.mojang_url["name_history"].format(uuid))
        assert json is not None
        if changed_at is True:
            return json
        if isinstance(json, list):
            return [data["name"] for data in json]
        raise ValueError(
            "How did this error happen?!?!?!?! "
            "Please post a bug at https://github.com/janaSunrise/HypixelIO"
        )

    @classmethod
    async def get_avatar(
        cls, name: t.Optional[str] = None, uuid: t.Optional[str] = None
    ) -> str:
        """
        Get the avatar of the specified player.

        Parameters
        ----------
        name: t.Optional[str]
            The username of the player. Defaults to None.
        uuid: t.Optional[str]
            The UUID of the player. Defaults to None.

        Returns
        -------
        str
            The URL containing the image of the avatar.
        """
        uuid = await cls._filter_name_uuid(name, uuid)
        await Utils._crafatar_fetch(Utils.url["avatar"].format(uuid))

        return Utils._form_crafatar_url(Utils.url["avatar"].format(uuid))

    @classmethod
    async def get_head(
        cls, name: t.Optional[str] = None, uuid: t.Optional[str] = None
    ) -> str:
        """
        Get the head skin of the specified player.

        Parameters
        ----------
        name: t.Optional[str]
            The username of the player. Defaults to None.
        uuid: t.Optional[str]
            The UUID of the player. Defaults to None.

        Returns
        -------
        str
            The URL containing the image of the head.
        """
        uuid = await cls._filter_name_uuid(name, uuid)
        await Utils._crafatar_fetch(Utils.url["head"].format(uuid))

        return Utils._form_crafatar_url(Utils.url["head"].format(uuid))

    @classmethod
    async def get_body(
        cls, name: t.Optional[str] = None, uuid: t.Optional[str] = None
    ) -> str:
        """
        Get the whole body's skin of the specified player

        Parameters
        ----------
        name: t.Optional[str]
            The username of the player. Defaults to None.
        uuid: t.Optional[str]
            The UUID of the player. Defaults to None.

        Returns
        -------
        str
            The URL containing the image of the whole body.
        """
        uuid = await cls._filter_name_uuid(name, uuid)
        await Utils._crafatar_fetch(Utils.url["body"].format(uuid))

        return Utils._form_crafatar_url(Utils.url["body"].format(uuid))
