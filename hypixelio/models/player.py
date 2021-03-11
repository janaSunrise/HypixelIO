import typing as t


class Player:
    """The Custom Hypixel Player Model."""
    def __init__(self, data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The JSON data received from the Hypixel API.
        """
        self.HYPIXEL_ID = data["_id"]
        self.UUID = data["uuid"]
        self.NAME = data["displayname"]
        self.KNOWN_ALIASES = data["knownAliases"]

        self.FIRST_LOGIN = data["firstLogin"]
        self.LAST_LOGIN = data["lastLogin"]

        self.ONE_TIME_ACHIEVEMENTS = data["achievementsOneTime"]
        self.ACHIEVEMENT_POINTS = data["achievementPoints"]
        self.ACHIEVEMENTS = data["achievements"]

        self.EXPERIENCE = data["networkExp"]
        self.LEVEL = self._calc_player_level(self.EXPERIENCE)
        self.KARMA = data["karma"]
        self.MC_VERSION_RP = data.get("mcVersionRp")

        self.CHALLENGES = data["challenges"]["all_time"]
        self.MOST_RECENT_GAME = data["mostRecentGameType"]

        self.TOTAL_REWARDS = data.get("totalRewards")
        self.TOTAL_DAILY_REWARDS = data.get("totalDailyRewards")
        self.REWARD_STREAK = data.get("rewardStreak")
        self.REWARD_SCORE = data.get("rewardScore")
        self.REWARD_HIGH_SCORE = data.get("rewardHighScore")

        self.PET_STATS = data.get("petStats")
        self.CURRENT_GADGET = data.get("currentGadget")

        self.SOCIAL_MEDIA = data["socialMedia"]["links"]

    @staticmethod
    def _calc_player_level(xp: t.Union[float, int]) -> float:
        return 1 + (-8750.0 + (8750 ** 2 + 5000 * xp) ** 0.5) / 2500

    def __str__(self) -> str:
        return self.NAME

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} id="{self.HYPIXEL_ID}" name="{self.NAME}" exp="{self.EXPERIENCE}">'

    def __hash__(self) -> int:
        return hash(self.UUID)

    def __eq__(self, other: "Player") -> bool:
        return self.UUID == other.UUID

    def __gt__(self, other: "Player") -> bool:
        return self.ACHIEVEMENT_POINTS > other.ACHIEVEMENT_POINTS

    def __ge__(self, other: "Player") -> bool:
        return self.ACHIEVEMENT_POINTS >= other.ACHIEVEMENT_POINTS
