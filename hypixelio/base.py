import sys
import typing as t
from datetime import datetime, timedelta

from .endpoints import API_PATH
from .exceptions import HypixelAPIError, InvalidArgumentError, RateLimitError


class BaseClient:
    def __init__(self, api_key: t.Union[str, list]):
        # API endpoint
        self.url = API_PATH["HYPIXEL"]

        # Choosing random API Key
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
            "User-Agent": f"HypixelIO[v{hypixelio_version}] Client (https://github.com/janaSunrise/HypixelIO) "
                          f"Python/{python_version}"
        }

    # Define the dunder methods
    def __repr__(self):
        return f"<{self.__class__.__qualname__} requests_remaining={self.requests_remaining} total_requests=" \
               f"{self.total_requests} retry_after={self.retry_after}>"

    # Utility to update ratelimiting variables
    def _update_ratelimit(self, resp_headers: t.Any) -> None:  # Typing for resp_headers is dict and CaseInsensitiveDict
        if "RateLimit-Limit" in resp_headers:
            if self.total_requests == 0:
                self.total_requests = int(resp_headers["RateLimit-Limit"])

            self.requests_remaining = int(resp_headers["RateLimit-Remaining"])
            self._ratelimit_reset = datetime.now() + timedelta(seconds=int(resp_headers["RateLimit-Reset"]))

    # Utility to check if ratelimit has been hit
    def _is_ratelimit_hit(self) -> bool:
        is_ratelimit_hit = self.requests_remaining != -1 \
            and (self.requests_remaining == 0 and self._ratelimit_reset > datetime.now()) \
            or self.retry_after \
            and (self.retry_after > datetime.now())

        return is_ratelimit_hit

    # Utility to handle status code 429 [Ratelimit]
    def _handle_ratelimit(self, resp_headers: t.Any) -> None:  # Typing for resp_headers is dict and CaseInsensitiveDict
        self.requests_remaining = 0
        self.retry_after = datetime.now() + timedelta(seconds=int(resp_headers["Retry-After"]))

        # Raise error
        raise RateLimitError(
            f"Out of Requests! "
            f"{datetime.now() + timedelta(seconds=int(resp_headers['Retry-After']))}"
        )

    # Utility to handle raising error if API response is not successful.
    @staticmethod
    def _handle_api_failure(json: t.Any) -> None:
        reason = "Something in the API has problem."
        if json["cause"] is not None:
            reason += f" Reason given: {json['cause']}"

        raise HypixelAPIError(reason=reason)

    @staticmethod
    def _filter_name_uuid(name: t.Optional[str] = None, uuid: t.Optional[str] = None) -> str:
        from hypixelio import Converters

        if not name and not uuid:
            raise InvalidArgumentError("Please provide a named argument of the player's username or player's UUID.")

        if name:
            uuid = Converters.username_to_uuid(name)

        return uuid

    # Utility for keys
    def add_key(self, api_key: t.Union[str, list]) -> None:
        if isinstance(api_key, str):
            api_key = [api_key]

        for k in api_key:
            if k in self._api_key:
                continue
            self._api_key.append(k)

    def remove_key(self, api_key: t.Union[str, list]) -> None:
        if isinstance(api_key, str):
            api_key = [api_key]

        for k in api_key:
            if k not in self._api_key:
                continue
            self._api_key.remove(k)
