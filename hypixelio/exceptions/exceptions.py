"""
Provides a Module for defining the custom exceptions to be raised
during errors while interacting with the API through this library.
"""


class HypixelAPIError(Exception):
    """
    Raised When the Hypixel API is facing some problems.

    Attributes:
        reason (str):
            Reason for why The Hypixel error was caused.
    """

    def __init__(self, reason: str = "undefined") -> None:
        self.err = f"The Hypixel API had a problem [{reason}]"
        super().__init__(self.err)

    def __str__(self) -> str:
        return self.err


class RateLimitError(Exception):
    """
    Raised When the Hypixel API Rate limit is hit.

    Attributes:
        reason (str):
            Reason for why The Hypixel Rate Limit error occurred.
    """

    def __init__(self, reason: str = "undefined") -> None:
        self.err = f"You just hit the Rate Limit for the Hypixel API [{reason}]"
        super().__init__(self.err)

    def __str__(self) -> str:
        return self.err


class PlayerNotFoundError(Exception):
    """
    Raised When the Specified Player is not found.

    Attributes:
        reason (str):
            Reason for why the user search fails, and returns null.
        user (str):
            The user who's search failed.
    """

    def __init__(self, reason: str, user: str) -> None:
        self.err = "Invalid Player Name or UUID!"
        super().__init__(self.err)

        self.reason = reason
        self.user = user

    def __str__(self) -> str:
        return self.err


class GuildNotFoundError(Exception):
    """
    Raised When the Specified Guild is not found.

    Attributes:
        reason (str):
            Reason for why the guild search returned null.
    """

    def __init__(self, reason: str = "Undefined") -> None:
        self.err = f"Invalid Guild Name or UUID! [{reason}]"
        super().__init__(self.err)

    def __str__(self) -> str:
        return self.err


class InvalidArgumentError(Exception):
    """Raised when there is Invalid argument, or Any argument is not specified."""
    pass
