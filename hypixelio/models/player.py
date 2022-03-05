import typing as t
from dataclasses import dataclass

from hypixelio.utils import get_rank
from hypixelio.utils import unix_time_to_datetime


@dataclass
class PlayerSocialMedia:
    youtube: t.Optional[str]
    twitter: t.Optional[str]
    instagram: t.Optional[str]
    twitch: t.Optional[str]
    discord: t.Optional[str]
    hypixel_forums: t.Optional[str]

    # Convert JSON data to a PlayerSocialMedia object
    @classmethod
    def from_json(cls, data: t.Optional[dict]) -> t.Optional["PlayerSocialMedia"]:
        if not data:
            return None

        return cls(
            youtube=data.get("YOUTUBE"),
            twitter=data.get("TWITTER"),
            instagram=data.get("INSTAGRAM"),
            twitch=data.get("TWITCH"),
            discord=data.get("DISCORD"),
            hypixel_forums=data.get("HYPIXEL_FORUMS"),
        )


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
        self.known_aliases = data["knownAliases"]

        self.first_login = unix_time_to_datetime(data["firstLogin"])
        self.last_login = unix_time_to_datetime(data["lastLogin"])
        self.last_logout = unix_time_to_datetime(data["lastLogout"])

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

        self.social_media = PlayerSocialMedia.from_json(data.get("socialMedia", {}).get("links"))

        self.rank = self._get_rank(data)

    @staticmethod
    def _calc_player_level(xp: t.Union[float, int]) -> float:
        return 1 + (-8750.0 + (8750 ** 2 + 5000 * xp) ** 0.5) / 2500

    @staticmethod
    def _get_rank(data: dict) -> t.Optional[str]:
        return get_rank(
            data.get("rank"),
            data.get("prefix"),
            data.get("monthlyPackageRank"),
            data.get("newPackageRank"),
            data.get("packageRank"),
        )

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} id="{self.hypixel_id}" name="{self.name}" experience="{self.experience}">'

    def __hash__(self) -> int:
        return hash(self.uuid)

    def __eq__(self, other: "Player") -> bool:
        return self.uuid == other.uuid
