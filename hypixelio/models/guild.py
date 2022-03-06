from hypixelio.utils.time import unix_time_to_datetime


class Guild:
    def __init__(self, data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The JSON data received from the Hypixel API.
        """
        self.hypixel_id = data["_id"]
        self.name = data["name"]

        # Coins the guild holds
        self.coins = data["coins"]

        # When the guild was created
        self.created = unix_time_to_datetime(data["created"])

        # Member count of the guild
        self.members = data["members"]

        # Old ranking data, and experience
        self.legacy_ranking = data["legacyRanking"]
        self.experience = data["exp"]

        self.achievements = data["achievements"]
        self.experience_by_game = data["guildExpByGameType"]

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} id="{self.hypixel_id}" name="{self.name}" experience="{self.experience}">'

    def __hash__(self) -> int:
        return hash(self.hypixel_id)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Guild):
            return False
        return self.hypixel_id == other.name
