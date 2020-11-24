"""
Provides a Module for defining the custom exceptions to be raised
during errors while interacting with the API through this library.
"""

import typing as t


class HypixelAPIError(Exception):
    """
    Raised When the Hypixel API is facing some problems.
    """
    def __init__(self, reason: str = "undefined") -> None:
        """
        Constructor for the HypixelAPIError Exception.

        Args:
            reason (str, optional): The reason for the Error. Defaults to "undefined".
        """
        self.err = f"The Hypixel API had a problem [{reason}]"
        super().__init__(self.err)

    def __str__(self) -> str:
        return self.err


class RateLimitError(Exception):
    """
    Raised When the Hypixel API Rate limit is hit.
    """
    def __init__(self, reason: str = "undefined") -> None:
        """
        Constructor for the RateLimitError exception.

        Args:
            reason (str, optional): The reason for the Error. Defaults to "undefined".
        """
        self.err = f"You just hit the Rate Limit for the Hypixel API [{reason}]"
        super().__init__(self.err)

    def __str__(self) -> str:
        return self.err


class PlayerNotFoundError(Exception):
    """
    Raised When the Specified Player is not found.
    """
    def __init__(self, reason: str, user: t.Optional[str]) -> None:
        """
        The constructor for the PlayerNotFoundError exception.

        Args:
            reason (str): The reason for the error.
            user (t.Optional[str]): The user searched for, but not found.
        """
        self.err = "Invalid Player Name or UUID!"
        super().__init__(self.err)

        self.reason = reason
        self.user = user

    def __str__(self) -> str:
        return self.err


class GuildNotFoundError(Exception):
    """
    Raised When the Specified Guild is not found.
    """
    def __init__(self, reason: str = "undefined") -> None:
        """
        The constructor for the GuildNotFoundError exception.

        Args:
            reason (str, optional): The reason for the Error. Defaults to "undefined".
        """
        self.err = f"Invalid Guild Name or UUID! [{reason}]"
        super().__init__(self.err)

    def __str__(self) -> str:
        return self.err


class InvalidArgumentError(Exception):
    """Raised when there is Invalid argument, or Any argument is not specified."""
    pass


class MojangAPIError(Exception):
    """
    Raised When the Mojang API is facing some problems.
    """
    def __init__(self, reason: str = "undefined") -> None:
        """
        The constructor for the MojanAPIError Exception.

        Args:
            reason (str, optional): The reason for the Error. Defaults to "undefined".
        """
        self.err = f"The Mojang API had a problem [{reason}]"
        super().__init__(self.err)

    def __str__(self) -> str:
        return self.err
