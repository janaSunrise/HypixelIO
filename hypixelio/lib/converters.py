import typing as t

import requests

from hypixelio.exceptions.exceptions import (
    InvalidArgumentError,
    MojangAPIError
)
from hypixelio.utils.constants import (
    MOJANG_API,
    TIMEOUT
)


class Converters:
    @classmethod
    def _fetch(cls, url: str) -> t.Optional[dict]:
        """
        This is the function for fetching the JSON from the Mojang API.

        Args:
            url (str): The Mojang URL, whose JSON is supposed to be fetched.

        Raises:
            InvalidArgumentError: Raised When there is an invalid URL, or Respone, whose code is not 200.
            MojangAPIError: Raised when the Mojang API is facing some problems, or there is some issues with the status.

        Returns:
            t.Optional[dict]: The JSON response from the Mojang API, Which is returned.
        """
        with requests.get(f"{MOJANG_API}{url}", timeout=TIMEOUT) as response:
            if response.status_code != 200:
                raise InvalidArgumentError("Invalid Username/UUID passed for conversion!")

            try:
                json = response.json()
                return json
            except Exception:
                raise MojangAPIError("There seems to be some problem with the content type or the API IS down.")

    @classmethod
    def username_to_uuid(cls, username: str) -> str:
        """
        This is a method, to convert username in minecraft, for its respective UUID.

        Args:
            username (str): This is the minecraft user, which is passed to this function for the UUID Conversion.

        Raises:
            MojangAPIError: Raised when there seems to be some problem with the Mojang API, which is contacted,
            for this conversion.

        Returns:
            str: returns the converted UUID for the respective username.
        """
        json = Converters._fetch(f"/users/profiles/minecraft/{username}")

        if "error" in json:
            raise MojangAPIError(f"An error occurred! {json['errorMessage']}")

        return json["id"]

    @classmethod
    def uuid_to_username(cls, uuid: str) -> str:
        """
        This is the function that converts the UUID for your profile, to the Username for your Minecraft account.

        Args:
            uuid (str): This is the minecraft UUID, which is passed to this function for the UUID to username Conversion.

        Raises:
            MojangAPIError: Raised when there seems to be some problem with the Mojang API, which is contacted,
            for this conversion.

        Returns:
            str: The username for the respective minecraft UUID is returned.
        """
        json = Converters._fetch(f"/user/profiles/{uuid}/names")

        if "error" in json:
            raise MojangAPIError(f"An error occurred! {json['errorMessage']}")

        return json[-1]["name"]
