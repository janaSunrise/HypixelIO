"""This module is dedicated to definition of the Player class."""

# KEY: f3acc46a-d48d-4014-8f81-6ddc9dc661c7


class Player:
    """
    This is the definition of the Custom Hypixel Player Model.

    Attributes
    ----------
    hypixel_id: str
    uuid: str
    display_name: str
    first_login: int
    last_login: int
    one_time_achievements: list
    achievement_points: int
    achievements: dict
    network_exp: int
    challenges: dict
    most_recent_game: str
    social_media: dict
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
