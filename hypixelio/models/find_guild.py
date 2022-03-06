class FindGuild:
    def __init__(self, data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The JSON data received from the Hypixel API.
        """
        self.id = data["guild"]  # pylint: disable=invalid-name

    def __str__(self) -> str:
        return self.id

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} id="{self.id}">'

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, FindGuild):
            return False
        return self.id == other.id
