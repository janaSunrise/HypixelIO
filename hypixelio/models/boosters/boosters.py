import typing as t

from .booster_info import BoosterInfo


class Boosters:
    """The the Custom Hypixel API Boosters Model."""
    def __init__(self, boosters: list, json: dict) -> None:
        """
        Parameters
        ----------
        boosters: list
            The list of the Coin Boosters in the Hypixel server.
        """
        self.BOOSTERS = [BoosterInfo(booster) for booster in boosters]
        self.STATE = json["boosterState"]

    def __len__(self) -> int:
        return len(self.BOOSTERS)

    def __getitem__(self, key: int) -> BoosterInfo:
        return self.BOOSTERS[key]

    def __setitem__(self, key: int, value: BoosterInfo) -> None:
        self.BOOSTERS[key] = value

    def __iter__(self) -> t.Iterator:
        return iter(self.BOOSTERS)

    def __eq__(self, other: "Boosters") -> bool:
        if len(self.BOOSTERS) != len(other.BOOSTERS):
            return False

        for booster in list(zip(self.BOOSTERS, other.BOOSTERS)):
            if booster[0].ID != booster[1].ID:
                return False
        return True

    def __str__(self) -> str:
        return str(len(self.BOOSTERS))

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} booster_count={len(self.BOOSTERS)}>"
