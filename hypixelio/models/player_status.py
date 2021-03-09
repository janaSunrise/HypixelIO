class PlayerStatus:
    def __init__(self, data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The JSON data received from the Hypixel API.
        """
        self.UUID = data["uuid"]
        self.SESSION_INFO = data["session"]

    def __str__(self) -> str:
        return self.UUID

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} uuid="{self.UUID}" online="{self.SESSION_INFO["online"]}">'

    def __hash__(self) -> int:
        return hash(self.UUID)

    def __eq__(self, other: "PlayerStatus") -> bool:
        return self.UUID == other.UUID
