class PlayerStatus:
    def __init__(self, data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The JSON data received from the Hypixel API.
        """
        self.uuid = data["uuid"]

        self.online = data["session"]["online"]
        self.game_type = data["session"].get("gameType")
        self.mode = data["session"].get("mode")
        self.map = data["session"].get("map")

    def __str__(self) -> str:
        return self.uuid

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} uuid="{self.uuid}" online="{self.online}">'

    def __hash__(self) -> int:
        return hash(self.uuid)

    def __eq__(self, other: "PlayerStatus") -> bool:
        return self.uuid == other.uuid
