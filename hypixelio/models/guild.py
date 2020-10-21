"""This module is dedicated to definition of the Guild class."""


class Guild:
    """
    This is the Custom Hypixel Guild Model.

    Attributes:
        data (dict): This contains the Returned JSON Response for the Guild API Request.
    """
    def __init__(
        self,
        data: dict
    ) -> None:
        self.HYPIXEL_ID = data["_id"]
        self.NAME = data["name"]
        self.COINS = data["coins"]
        self.CREATED = data["members"]

        self.MEMBERS = data["created"]

        self.LEGACY_RANKING = data["legacyRanking"]
        self.EXPERIENCE = data["exp"]

        self.ACHIEVEMENTS = data["achievements"]
        self.EXPERIENCE_BY_GAME = data["guildExpByGameType"]
