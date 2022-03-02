import typing as t

from hypixelio.utils.time import unix_time_to_datetime


class Player:
    def __init__(self, data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The JSON data received from the Hypixel API.
        """
        self.hypixel_id = data["_id"]
        self.uuid = data["uuid"]

        self.name = data["displayname"]
        self.known_aliase = data["knownAliases"]

        self.first_login = unix_time_to_datetime(data["firstLogin"])
        self.last_login = unix_time_to_datetime(data["lastLogin"])

        self.one_time_achievements = data["achievementsOneTime"]
        self.achievement_points = data["achievementPoints"]
        self.achievements = data["achievements"]

        self.experience = data["networkExp"]
        self.level = self._calc_player_level(self.experience)

        self.karma = data["karma"]
        self.mc_version_rp = data.get("mcVersionRp")

        self.challenges = data["challenges"]["all_time"]
        self.most_recent_game = data["mostRecentGameType"]

        self.total_rewards = data.get("totalRewards")
        self.total_daily_rewards = data.get("totalDailyRewards")
        self.reward_streak = data.get("rewardStreak")
        self.reward_score = data.get("rewardScore")
        self.reward_high_score = data.get("rewardHighScore")

        self.pet_stats = data.get("petStats")
        self.current_gadget = data.get("currentGadget")

        self.social_media = data["socialMedia"]["links"]

    @staticmethod
    def _calc_player_level(xp: t.Union[float, int]) -> float:
        return 1 + (-8750.0 + (8750 ** 2 + 5000 * xp) ** 0.5) / 2500

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} id="{self.hypixel_id}" name="{self.name}" experience="{self.experience}">'

    def __hash__(self) -> int:
        return hash(self.uuid)

    def __eq__(self, other: "Player") -> bool:
        return self.uuid == other.uuid
