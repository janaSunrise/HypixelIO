class PlayerStatus:
    def __init__(self, data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The JSON data received from the Hypixel API.
        """
        self.uuid = data["uuid"]
        self.session_info = data["session"]

    def __str__(self) -> str:
        return self.uuid

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} uuid="{self.uuid}" online="{self.session_info["online"]}">'

    def __hash__(self) -> int:
        return hash(self.uuid)

    def __eq__(self, other: "PlayerStatus") -> bool:
        return self.uuid == other.uuid
