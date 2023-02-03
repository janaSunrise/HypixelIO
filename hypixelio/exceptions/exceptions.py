"""Custom exceptions used for the librar."""
__all__ = (
    "InvalidArgumentError",
    "PlayerNotFoundError",
    "HypixelAPIError",
    "RateLimitError",
    "GuildNotFoundError",
    "CrafatarAPIError",
    "MojangAPIError",
)

import typing as t
from datetime import datetime


class InvalidArgumentError(Exception):
    """Raised when invalid argument is present, or no argument is specified."""

    ...


# API exceptions
class APIError(Exception):
    """Base class for all API exceptions."""

    def __init__(self, service: str, reason: t.Optional[str] = None) -> None:
        """
        Parameters
        ----------
        reason: str
            The reason for the Error. Defaults to None.
        """
        error = f"There was an issue with the {service} API."
        if reason:
            error += f" Reason: {reason}."

        super().__init__(error)
        self.error = error

    def __str__(self) -> str:
        return self.error


class HypixelAPIError(APIError):
    """Raised when there is an issue with the Hypixel API or during fetch."""

    def __init__(self, reason: t.Optional[str] = None) -> None:
        """
        Parameters
        ----------
        reason: str
            The reason for the Error. Defaults to None.
        """
        super().__init__("Hypixel", reason)


class CrafatarAPIError(APIError):
    """Raised during issues faced by Crafatar API."""

    def __init__(self, reason: t.Optional[str] = None) -> None:
        """
        Parameters
        ----------
        reason: str
            The reason for the Error. Defaults to None.
        """
        super().__init__("Crafatar", reason)


class MojangAPIError(APIError):
    """Raised when the Mojang API is facing some problems."""

    def __init__(self, reason: t.Optional[str] = None) -> None:
        """
        Parameters
        ----------
        reason: str
            The reason for the Error. Defaults to None.
        """
        super().__init__("Mojang", reason)


# Rate-limit exception
class RateLimitError(Exception):
    """Raised when the Rate-limit for the Hypixel API is hit."""

    def __init__(self, retry_after: datetime) -> None:
        """
        Parameters
        ----------
        retry_after: datetime
            The time when the API will be available again for fetching.
        """
        error = (
            "The rate-limit for the Hypixel API was hit. Try again after"
            f"{retry_after.strftime('%Y-%m-%d %H:%M:%S')}."
        )

        super().__init__(error)
        self.error = error

    def __str__(self) -> str:
        return self.error


# Hypixel-related exceptions
class PlayerNotFoundError(Exception):
    """Raised when the specified player is not found."""

    def __init__(
        self, reason: t.Optional[str] = None, user: t.Optional[str] = None
    ) -> None:
        """
        Parameters
        ----------
        reason: str
            The reason for the error.
        user: t.Optional[str]
            The user not found when searched for.
        """
        error = "Player not found."
        if reason:
            error += f" {reason}."

        super().__init__(error)

        self.error = error
        self.user = user

    def __str__(self) -> str:
        return self.error


class GuildNotFoundError(Exception):
    """Raised when the specified guild is not found."""

    def __init__(self, reason: t.Optional[str] = None) -> None:
        """
        Parameters
        ----------
        reason: str
            The reason for the Error. Defaults to None.
        """
        error = "Guild not found."
        if reason:
            error += f" {reason}."

        super().__init__(error)
        self.error = error

    def __str__(self) -> str:
        return self.error
