"""This module is dedicated to definition of the Find Guild class."""


class FindGuild:
    """
    This is the Custom Hypixel Find Guild Model.

    Attributes:
        data (dict): This contains the Returned JSON Response for the Find Guild API Request.
    """
    def __init__(
        self,
        data: dict
    ) -> None:
        self.ID = data["guild"]

    def __str__(self) -> str:
        return self.ID

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} id="{self.ID}">'
