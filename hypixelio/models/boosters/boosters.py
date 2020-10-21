"""This module is dedicated to definition of the Boosters class."""

from .booster_info import BoosterInfo


class Boosters:
    """
    This is the definition of the Custom Hypixel API Boosters Model.
    """
    def __init__(
        self,
        boosters: list,
    ) -> None:
        self.BOOSTERS = [BoosterInfo(booster) for booster in boosters]
