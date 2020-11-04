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
        with requests.get(f"{MOJANG_API}{url}", timeout=TIMEOUT) as response:
            if response.status_code != 200:
                raise InvalidArgumentError("Invalid Username/UUID passed for conversion!")

            try:
                json = response.json()
                return json
            except Exception as e:
                raise MojangAPIError("There seems to be some problem with the content type or the API IS down.")

    @classmethod
    def username_to_uuid(cls, username: str) -> str:
        json = Converters._fetch(f"/users/profiles/minecraft/{username}")

        if "error" in json:
            raise MojangAPIError(f"An error occurred! {json['errorMessage']}")

        return json["id"]

    @classmethod
    def uuid_to_name(cls, uuid: str) -> str:
        json = Converters._fetch(f"/user/profiles/{uuid}/names")

        if "error" in json:
            raise MojangAPIError(f"An error occurred! {json['errorMessage']}")

        return json["name"]
