"""This module is dedicated to definition of the Custom Player class."""


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
        hypixel_id: str,
        uuid: str,
        display_name: str,
        known_aliases: str,
        first_login: int,
        last_login: int,
        one_time_achievements: list,
        achievement_points: int,
        achievements: dict,
        network_exp: int,
        challenges: dict,
        most_recent_game: str,
        social_media: dict
    ) -> None:
        self.HYPIXEL_ID = hypixel_id
        self.UUID = uuid
        self.DISPLAY_NAME = display_name
        self.KNOWN_ALIASES = known_aliases

        self.FIRST_LOGIN = first_login
        self.LAST_LOGIN = last_login

        self.ONE_TIME_ACHIEVEMENTS = one_time_achievements
        self.ACHIEVEMENT_POINTS = achievement_points
        self.ACHIEVEMENTS = achievements

        self.EXPERIENCE = network_exp

        self.CHALLENGES = challenges["all_time"]
        self.MOST_RECENT_GAME = most_recent_game

        self.SOCIAL_MEDIA = social_media["links"]
