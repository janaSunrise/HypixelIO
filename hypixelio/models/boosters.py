from typing import Any, Dict, Iterator, List

from hypixelio.utils import unix_time_to_datetime


class BoosterInfo:
    def __init__(self, info: Dict[str, Any]) -> None:
        """
        Parameters
        ----------
        info: dict
            This contains the JSON Response from the API for the Info about a specific booster.
        """
        self.id = info["_id"]
        self.purchaser_uuid = info["purchaserUuid"]

        self.amount = info["amount"]
        self.original_length = info["originalLength"]
        self.length = info["length"]

        self.game_type_code = info["gameType"]
        self.date_activated = unix_time_to_datetime(info["dateActivated"])

        self.stacked = "stacked" in info

    def __eq__(self, other: "BoosterInfo") -> bool:
        return self.id == other.id and self.purchaser_uuid == other.purchaser_uuid

    def __hash__(self) -> int:
        return hash((self.id, self.purchaser_uuid))

    def __str__(self) -> str:
        return self.purchaser_uuid

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} id="{self.id}" purchaser="{self.purchaser_uuid}" stacked={self.stacked}>'


class Boosters:
    def __init__(self, boosters: List[Dict[str, Any]], json: Dict[str, Any]) -> None:
        """
        Parameters
        ----------
        boosters: list
            The list of the Coin Boosters in the Hypixel server.
        """
        # All the boosters
        self.boosters = [BoosterInfo(booster) for booster in boosters]

        # State of the boosters
        self.state = json["boosterState"]

        # Decrementing
        self.decrementing = self.state["decrementing"]

    def __len__(self) -> int:
        return len(self.boosters)

    def __getitem__(self, key: int) -> BoosterInfo:
        return self.boosters[key]

    def __setitem__(self, key: int, value: BoosterInfo) -> None:
        self.boosters[key] = value

    def __iter__(self) -> Iterator:
        return iter(self.boosters)

    def __eq__(self, other: "Boosters") -> bool:
        if len(self.boosters) != len(other.boosters):
            return False

        for booster in list(zip(self.boosters, other.boosters)):
            if booster[0].id != booster[1].id:
                return False

        return True

    def __str__(self) -> str:
        return str(len(self.boosters))

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} booster_count={len(self.boosters)}>"
