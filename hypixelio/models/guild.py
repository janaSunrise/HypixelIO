"""This module is dedicated to definition of the Guild class."""


class Guild:
    """
    This is the definition of the Custom Hypixel Guild Model.
    """
    def __init__(
        self,
        hypixel_id: str,
        name: str,
        coins: int,
        members: list,
        created: int,
        legacy_ranking: int,
        experience: int,
        achievements: dict,
        experience_by_game: dict
    ) -> None:
        self.HYPIXEL_ID = hypixel_id
        self.NAME = name
        self.COINS = coins
        self.CREATED = created

        self.MEMBERS = members

        self.LEGACY_RANKING = legacy_ranking
        self.EXPERIENCE = experience

        self.ACHIEVEMENTS = achievements
        self.EXPERIENCE_BY_GAME = experience_by_game
