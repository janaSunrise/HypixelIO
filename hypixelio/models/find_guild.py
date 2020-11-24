"""This module is dedicated to definition of the Find Guild class."""


class FindGuild:
    """
    This is the Custom Hypixel Find Guild Model.
    """
    def __init__(
        self,
        data: dict
    ) -> None:
        """
        The constructor for the Hypixel Find Guild Model.

        Args:
            data (dict): The JSON data received from the Hypixel API.
        """
        self.ID = data["guild"]

    def __str__(self) -> str:
        return self.ID

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} id="{self.ID}">'

    def __hash__(self) -> int:
        return hash(self.ID)

    def __eq__(self, other: "FindGuild") -> bool:
        return self.ID == other.ID
