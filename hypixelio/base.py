import sys
from datetime import datetime, timedelta
from typing import Any, Dict, Optional, Union

from .endpoints import API_PATH
from .exceptions import HypixelAPIError, InvalidArgumentError, RateLimitError


# TODO: Move to `requests.session` for better performance and avoid creating a new session for every request.
class BaseClient:
    def __init__(self, api_key: Union[str, list]):
        self.url = API_PATH["HYPIXEL"]

        if not isinstance(api_key, list):
            self._api_key = [api_key]

        # Ratelimiting config
        self.requests_remaining = -1
        self.total_requests = 0
        self._ratelimit_reset = datetime(1998, 1, 1)
        self.retry_after = datetime(1998, 1, 1)

        # Headers
        from hypixelio import __version__ as hypixelio_version

        python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        self.headers = {
            "User-Agent": f"HypixelIO v{hypixelio_version} Client (https://github.com/janaSunrise/HypixelIO) "
            f"Python/{python_version}"
        }

    # Define the dunder methods
    def __repr__(self):
        return (
            f"<{self.__class__.__qualname__} requests_remaining={self.requests_remaining} total_requests="
            f"{self.total_requests} retry_after={self.retry_after}>"
        )

    # Utility to update ratelimiting variables
    def _update_ratelimit(self, resp_headers: Dict[str, Any]) -> None:
        if "RateLimit-Limit" in resp_headers:
            if self.total_requests == 0:
                self.total_requests = int(resp_headers["RateLimit-Limit"])

            self.requests_remaining = int(resp_headers["RateLimit-Remaining"])
            self._ratelimit_reset = datetime.now() + timedelta(
                seconds=int(resp_headers["RateLimit-Reset"])
            )

    # Utility to check if ratelimit has been hit
    def _is_ratelimit_hit(self) -> bool:
        is_ratelimit_hit = self.requests_remaining != -1 \
            and (self.requests_remaining == 0 and self._ratelimit_reset > datetime.now()) \
            or self.retry_after \
            and (self.retry_after > datetime.now())

        return is_ratelimit_hit

    # Handle ratelimitiing
    def _handle_ratelimit(self, resp_headers: Dict[str, Any]) -> None:
        self.requests_remaining = 0
        self.retry_after = datetime.now() + timedelta(
            seconds=int(resp_headers["Retry-After"])
        )

        raise RateLimitError(self.retry_after)

    # Handle raising error if API response is not successful.
    @staticmethod
    def _handle_api_failure(json: Dict[str, Any]) -> None:
        raise HypixelAPIError(reason=json["cause"])

    # TODO: Refactor this w/ function overloading and clean code if possible.
    # TODO: Potential issue, the code used to fetch is blocking. Not good for async.
    @staticmethod
    def _filter_name_uuid(
        name: Optional[str] = None, uuid: Optional[str] = None
    ) -> str:
        from hypixelio import Converters

        if not name and not uuid:
            raise InvalidArgumentError(
                "Named argument for player's either username or UUID not found."
            )

        if name:
            uuid = Converters.username_to_uuid(name)

        return uuid  # type: ignore

    # Utility for keys
    def add_key(self, api_key: Union[str, list]) -> None:
        """
        Add a Hypixel API Key to the list of the API keys.

        Parameters
        ----------
        api_key: Union[str, list]
            The API key(s) to be added to the lis

        Returns
        -------
            None
        """
        if isinstance(api_key, str):
            api_key = [api_key]

        for key in api_key:
            if key in self._api_key:
                continue

            self._api_key.append(key)

    def remove_key(self, api_key: Union[str, list]) -> None:
        """
        Remove a Hypixel API Key from the list of the API keys.

        Parameters
        ----------
        api_key: Union[str, list]
            The API key(s) to be removed from the lis

        Returns
        -------
            None
        """
        if isinstance(api_key, str):
            api_key = [api_key]

        for key in api_key:
            if key not in self._api_key:
                continue

            self._api_key.remove(key)
