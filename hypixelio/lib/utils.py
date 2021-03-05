import typing as t

import requests
from requests.models import Response

from hypixelio.exceptions.exceptions import (
    CrafatarAPIError,
    InvalidArgumentError,
    MojangAPIError,
)
from hypixelio.lib.converters import (
    Converters
)
from hypixelio.utils.constants import (
    MOJANG_API,
    TIMEOUT
)


class Utils:
    @classmethod
    def _fetch(cls, url: str) -> t.Optional[dict]:
        """
        This is the function for fetching the JSON from the Mojang API.

        Args:
            url (str): The Mojang URL, whose JSON is supposed to be fetched.

        Raises:
            InvalidArgumentError: Raised When there is an invalid URL, or Response, whose code is not 200.
            MojangAPIError: Raised when the Mojang API is facing some problems, or there is some issues with the status.

        Returns:
            t.Optional[dict]: The JSON response from the Mojang API, Which is returned.
        """
        with requests.get(f"{MOJANG_API}{url}", timeout=TIMEOUT) as response:
            if response.status_code != 200:
                raise InvalidArgumentError("Invalid data passed for conversion!")

            try:
                json = response.json()
                return json
            except Exception:
                raise MojangAPIError("There seems to be some problem with the content type or the API IS down.")

    @classmethod
    def _crafatar_fetch(cls, url: str) -> Response:
        """
        This is the function for fetching the JSON from the Crafatar API.

        Args:
            url (str): The Crafatar URL, whose JSON is supposed to be fetched.

        Raises:
            InvalidArgumentError: Raised When there is an invalid URL, or Response, whose code is not 200.
            CrafatarAPIError: Raised when the Crafatar API is facing some problems, or there is some issues with the
                              status.

        Returns:
            t.Optional[dict]: The JSON response from the Crafatar API, Which is returned.
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

        Args:
            route (str): The URL path to visit.

        Returns:
            str: The well formed API URL for fetching.
        """
        return f"https://crafatar.com/{route}"

    @classmethod
    def get_name_history(
            cls, name: t.Optional[str] = None, uuid: t.Optional[str] = None, changed_at: bool = False
    ) -> t.Union[list, dict]:
        """
        This get the name history with records of a player.

        Args:
            name (t.Optional[str], optional): The username of the player. Defaults to None.
            uuid (t.Optional[str], optional): The UUID of the player. Defaults to None.
            changed_at (bool, optional): Toggle to true, if you need when the player changed name. Defaults to False.

        Raises:
            InvalidArgumentError: Raised if neither UUID or username isn't passed.

        Returns:
            t.Union[list, dict]: The list or dictionary with the name history and records.
        """
        if name:
            uuid = Converters.username_to_uuid(name)
            json = Utils._fetch(f"/user/profiles/{uuid}/names")
        elif uuid:
            json = Utils._fetch(f"/user/profiles/{uuid}/names")
        else:
            raise InvalidArgumentError("Please provide a Named argument of the User's name or UUID.")

        if changed_at:
            return json
        else:
            usernames = []
            for data in json:
                usernames.append(data["name"])

            return usernames

    @classmethod
    def get_avatar(cls, name: t.Optional[str] = None, uuid: t.Optional[str] = None) -> str:
        """
        Get the avatar of the specified player

        Args:
            name (t.Optional[str], optional): The username of the player. Defaults to None.
            uuid (t.Optional[str], optional): The UUID of the player. Defaults to None.

        Raises:
            InvalidArgumentError: Raised if neither UUID or username isn't passed.

        Returns:
            str: The URL containing the image of the avatar.
        """
        url = "/avatars/{}"

        if name:
            uuid = Converters.username_to_uuid(name)
            Utils._crafatar_fetch(url.format(uuid))
        elif uuid:
            Utils._crafatar_fetch(url.format(uuid))
        else:
            raise InvalidArgumentError("Please provide a Named argument of the User's name or UUID.")

        return Utils._form_crafatar_url(url.format(uuid))

    @classmethod
    def get_head(cls, name: t.Optional[str] = None, uuid: t.Optional[str] = None) -> str:
        """
        Get the head skin of the specified player

        Args:
            name (t.Optional[str], optional): The username of the player. Defaults to None.
            uuid (t.Optional[str], optional): The UUID of the player. Defaults to None.

        Raises:
            InvalidArgumentError: Raised if neither UUID or username isn't passed.

        Returns:
            str: The URL containing the image of the head.
        """
        url = "/renders/head/{}"

        if name:
            uuid = Converters.username_to_uuid(name)
            Utils._crafatar_fetch(url.format(uuid))
        elif uuid:
            Utils._crafatar_fetch(url.format(uuid))
        else:
            raise InvalidArgumentError("Please provide a Named argument of the User's name or UUID.")

        return Utils._form_crafatar_url(url.format(uuid))

    @classmethod
    def get_body(cls, name: t.Optional[str] = None, uuid: t.Optional[str] = None) -> str:
        """
        Get the whole body's skin of the specified player

        Args:
            name (t.Optional[str], optional): The username of the player. Defaults to None.
            uuid (t.Optional[str], optional): The UUID of the player. Defaults to None.

        Raises:
            InvalidArgumentError: Raised if neither UUID or username isn't passed.

        Returns:
            str: The URL containing the image of the whole body.
        """
        url = "/renders/body/{}"

        if name:
            uuid = Converters.username_to_uuid(name)
            Utils._crafatar_fetch(url.format(uuid))
        elif uuid:
            Utils._crafatar_fetch(url.format(uuid))
        else:
            raise InvalidArgumentError("Please provide a Named argument of the User's name or UUID.")

        return Utils._form_crafatar_url(url.format(uuid))
