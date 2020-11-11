"""This module is dedicated to definition of the Player class."""


class Player:
    """
    This is the Custom Hypixel Player Model.

    Attributes:
        data (dict): This contains the Returned JSON Response for the Player API Request.
    """
    def __init__(
        self,
        data: dict
    ) -> None:
        self.HYPIXEL_ID = data["_id"]
        self.UUID = data["uuid"]
        self.DISPLAY_NAME = data["displayname"]
        self.KNOWN_ALIASES = data["knownAliases"]

        self.FIRST_LOGIN = data["firstLogin"]
        self.LAST_LOGIN = data["lastLogin"]

        self.ONE_TIME_ACHIEVEMENTS = data["achievementsOneTime"]
        self.ACHIEVEMENT_POINTS = data["achievementPoints"]
        self.ACHIEVEMENTS = data["achievements"]

        self.EXPERIENCE = data["networkExp"]

        self.CHALLENGES = data["challenges"]["all_time"]
        self.MOST_RECENT_GAME = data["mostRecentGameType"]

        self.SOCIAL_MEDIA = data["socialMedia"]["links"]

    def __str__(self) -> str:
        return self.DISPLAY_NAME

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} id="{self.HYPIXEL_ID}" name="{self.DISPLAY_NAME}" exp="{self.EXPERIENCE}">'

    def __hash__(self) -> int:
        return hash(self.UUID)

    def __eq__(self, other: "Player") -> bool:
        return self.UUID == other.UUID

    def __gt__(self, other: "Player") -> bool:
        return self.ACHIEVEMENT_POINTS > other.ACHIEVEMENT_POINTS

    def __ge__(self, other: "Player") -> bool:
        return self.ACHIEVEMENT_POINTS >= other.ACHIEVEMENT_POINTS
