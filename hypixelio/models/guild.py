class Guild:
    """The the Custom Hypixel Guild Model."""
    def __init__(self, data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The JSON data received from the Hypixel API.
        """
        self.HYPIXEL_ID = data["_id"]
        self.NAME = data["name"]
        self.COINS = data["coins"]
        self.CREATED = data["members"]

        self.MEMBERS = data["created"]

        self.LEGACY_RANKING = data["legacyRanking"]
        self.EXPERIENCE = data["exp"]

        self.ACHIEVEMENTS = data["achievements"]
        self.EXPERIENCE_BY_GAME = data["guildExpByGameType"]

        self.MEMBERS = data["members"]

    def __str__(self) -> str:
        return self.NAME

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} id="{self.HYPIXEL_ID}" name="{self.NAME}" exp="{self.EXPERIENCE}">'

    def __hash__(self) -> int:
        return hash(self.HYPIXEL_ID)

    def __eq__(self, other: "Guild") -> bool:
        return self.HYPIXEL_ID == other.HYPIXEL_ID

    def __gt__(self, other: "Guild") -> bool:
        return self.EXPERIENCE > other.EXPERIENCE

    def __ge__(self, other: "Guild") -> bool:
        return self.EXPERIENCE >= other.EXPERIENCE
