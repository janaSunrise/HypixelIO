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
        url: str
            The Crafatar URL, whose JSON is supposed to be fetched.

        Returns
        -------
        t.Optional[dict]
            The JSON response from the Crafatar API, which is returned.
        """
        with requests.get(f"https://crafatar.com/{url}", timeout=TIMEOUT) as response:
            if response.status_code == 422:
                raise InvalidArgumentError("Invalid data passed for conversion!")

            try:
                return response
            except Exception:
                raise CrafatarAPIError("There seems to be some problem with the content type or the API IS down.")

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
            cls, name: t.Optional[str] = None, uuid: t.Optional[str] = None, changed_at: bool = False
    ) -> t.Union[list, dict]:
        """
        This get the name history with records of a player.

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
        if name:
            uuid = Converters.username_to_uuid(name)
            json = Converters._fetch(Utils.mojang_url["name_history"].format(uuid))
        elif uuid:
            json = Converters._fetch(Utils.mojang_url["name_history"].format(uuid))
        else:
            raise InvalidArgumentError("Please provide a Named argument of the User's name or UUID.")

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
        name: t.Optional[str]
            The username of the player. Defaults to None.
        uuid: t.Optional[str]
            The UUID of the player. Defaults to None.

        Returns
        -------
        str
            The URL containing the image of the avatar.
        """
        if name:
            uuid = Converters.username_to_uuid(name)
            Utils._crafatar_fetch(Utils.url["avatar"].format(uuid))
        elif uuid:
            Utils._crafatar_fetch(Utils.url["avatar"].format(uuid))
        else:
            raise InvalidArgumentError("Please provide a Named argument of the User's name or UUID.")

        return Utils._form_crafatar_url(Utils.url["avatar"].format(uuid))

    @classmethod
    def get_head(cls, name: t.Optional[str] = None, uuid: t.Optional[str] = None) -> str:
        """
        Get the head skin of the specified player

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
        if name:
            uuid = Converters.username_to_uuid(name)
            Utils._crafatar_fetch(Utils.url["head"].format(uuid))
        elif uuid:
            Utils._crafatar_fetch(Utils.url["head"].format(uuid))
        else:
            raise InvalidArgumentError("Please provide a Named argument of the User's name or UUID.")

        return Utils._form_crafatar_url(Utils.url["head"].format(uuid))

    @classmethod
    def get_body(cls, name: t.Optional[str] = None, uuid: t.Optional[str] = None) -> str:
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
        if name:
            uuid = Converters.username_to_uuid(name)
            Utils._crafatar_fetch(Utils.url["body"].format(uuid))
        elif uuid:
            Utils._crafatar_fetch(Utils.url["body"].format(uuid))
        else:
            raise InvalidArgumentError("Please provide a Named argument of the User's name or UUID.")

        return Utils._form_crafatar_url(Utils.url["body"].format(uuid))
