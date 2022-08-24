__all__ = ("Utils",)


import typing as t

import requests
from requests.models import Response

from ..constants import TIMEOUT
from ..endpoints import API_PATH
from ..exceptions import (
    CrafatarAPIError,
    InvalidArgumentError,
)
from ..lib.converters import Converters


class Utils:
    mojang_url = API_PATH["MOJANG"]
    url = API_PATH["CRAFATAR"]

    @classmethod
    def _crafatar_fetch(cls, url: str) -> Response:
        """
        Method to fetch the JSON from the Crafatar API.

        Parameters
        ----------
        url: str
            The Crafatar URL, whose JSON is supposed to be fetched.

        Returns
        -------
        Response
            The JSON response from the Crafatar API.
        """
        with requests.get(f"https://crafatar.com/{url}", timeout=TIMEOUT) as response:
            if response.status_code == 422:
                raise InvalidArgumentError("Invalid URL passed. Either user does not exist, or URL is malformed.")

            try:
                return response
            except Exception:
                raise CrafatarAPIError()

    @staticmethod
    def _filter_name_uuid(
        name: t.Optional[str] = None,
        uuid: t.Optional[str] = None
    ) -> str:
        if name is None and uuid is None:
            raise InvalidArgumentError("Named argument for player's either username or UUID not found.")

        if name:
            uuid = Converters.username_to_uuid(name)

        return uuid  # type: ignore

    @classmethod
    def _form_crafatar_url(cls, route: str) -> str:
        """
        This function forms the crafatar API URL for fetching USER skins.

        Parameters
        ----------
        route: str
            The URL path to visit.

        Returns
        -------
        str
            The well formed API URL for fetching.
        """
        return f"https://crafatar.com{route}"

    @classmethod
    def get_name_history(
        cls,
        name: t.Optional[str] = None,
        uuid: t.Optional[str] = None,
        changed_at: bool = False,
    ) -> t.Union[list, dict]:
        """
        Get the name history with records of a player.

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
        uuid = cls._filter_name_uuid(name, uuid)
        json = Converters._fetch(Utils.mojang_url["name_history"].format(uuid))

        # Return JSON if time is specified.
        if changed_at:
            return json

        # Return all usernames.
        usernames = []
        for data in json:
            usernames.append(data["name"])

        return usernames

    @classmethod
    def get_avatar(
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
        uuid = cls._filter_name_uuid(name, uuid)
        Utils._crafatar_fetch(Utils.url["avatar"].format(uuid))

        return Utils._form_crafatar_url(Utils.url["avatar"].format(uuid))

    @classmethod
    def get_head(
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
        uuid = cls._filter_name_uuid(name, uuid)
        Utils._crafatar_fetch(Utils.url["head"].format(uuid))

        return Utils._form_crafatar_url(Utils.url["head"].format(uuid))

    @classmethod
    def get_body(
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
        uuid = cls._filter_name_uuid(name, uuid)
        Utils._crafatar_fetch(Utils.url["body"].format(uuid))

        return Utils._form_crafatar_url(Utils.url["body"].format(uuid))
