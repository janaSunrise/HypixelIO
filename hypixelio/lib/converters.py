__all__ = "Converters"

import typing as t

import requests

from hypixelio.endpoints import API_PATH
from hypixelio.exceptions.exceptions import (
    MojangAPIError,
    PlayerNotFoundError
)
from hypixelio.utils.constants import (
    MOJANG_API,
    TIMEOUT
)


class Converters:
    url = API_PATH["MOJANG"]

    @classmethod
    def _fetch(cls, url: str) -> t.Optional[dict]:
        """
        This is the internal function for fetching the JSON from the Mojang API.

        Parameters
        ----------
        url: `str`
            The Mojang URL, whose JSON is supposed to be fetched.

        Returns
        -------
        `t.Optional[dict]`
            The JSON response from the Mojang API, Which is returned.
        """
        with requests.get(f"{MOJANG_API}{url}", timeout=TIMEOUT) as response:
            if response.status_code == 204:
                raise PlayerNotFoundError("204 value returned during conversion to UUID.", None)

            if response.status_code == 400:
                raise PlayerNotFoundError("Badly formed UUID error.", None)

            try:
                json = response.json()
            except Exception:
                raise MojangAPIError("There seems to be some problem with the content type or the API is down.")
            else:
                if "error" in json:
                    raise MojangAPIError(f"An error occurred! {json['errorMessage']}")

                return json

    @classmethod
    def username_to_uuid(cls, username: str) -> str:
        """
        This is a method, to convert username in minecraft, for its respective UUID.

        Parameters
        ----------
        username: `str`
            This is the minecraft user, which is passed to this function for the UUID Conversion.

        Returns
        -------
        `str`
            returns the converted UUID for the respective username.
        """
        json = Converters._fetch(Converters.url["username_to_uuid"].format(username))

        return json["id"]

    @classmethod
    def uuid_to_username(cls, uuid: str) -> str:
        """
        This is the function that converts the UUID for your profile, to the Username for your Minecraft account.

        Parameters
        ----------
        uuid: `str`
            This is the minecraft UUID, which is passed to this function for the UUID to username Conversion.

        Returns
        -------
        `str`
            The username for the respective minecraft UUID is returned.
        """
        json = Converters._fetch(Converters.url["uuid_to_username"].format(uuid))

        return json[-1]["name"]
