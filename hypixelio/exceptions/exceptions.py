"""
Provides a Module for defining the custom expections to be raised
during errors while interacting with the API through this library.
"""


class HypixelAPIError(Exception):
    """Raised When the Hypixel API is facing some problems."""

    def __init__(self, reason: str = "undefined") -> None:
        self.err = f"The Hypixel API had a problem [{reason}]"
        super().__init__(self.err)

    def __str__(self) -> str:
        return self.err


class RateLimitError(Exception):
    """Raised When the Hypixel API is facing some problems."""

    def __init__(self, reason: str = "undefined") -> None:
        self.err = f"You just hit the Rate Limit for the Hypixel API [{reason}]"
        super().__init__(self.err)

    def __str__(self) -> str:
        return self.err


class PlayerNotFoundError(Exception):
    """Raised When the Specified Player is not found."""

    def __init__(self, reason: str, user: str) -> None:
        self.err = "Invalid Player Name or UUID!"
        super().__init__(self.err)

        self.reason = reason
        self.user = user

    def __str__(self) -> str:
        return self.err


class GuildNotFoundError(Exception):
    """Raised When the Specified Guild is not found."""

    def __init__(self, reason: str = "Undefined") -> None:
        self.err = f"Invalid Guild Name or UUID! [{reason}]"
        super().__init__(self.err)

    def __str__(self) -> str:
        return self.err


class InvalidArgumentError(Exception):
    pass
