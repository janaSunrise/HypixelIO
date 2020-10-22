"""This module is dedicated to definition of the Player class."""


class BoosterInfo:
    """
    This is the Custom Hypixel API Booster's Info Model.

    Attributes:
        info (dict): This contains the Returned JSON Response for the Booster's List Element API Request.
    """
    def __init__(
        self,
        info: dict
    ) -> None:
        self.ID = info["_id"]
        self.PURCHASER_UUID = info["purchaserUuid"]

        self.AMOUNT = info["amount"]
        self.ORIGINAL_LENGTH = info["originalLength"]
        self.LENGTH = info["length"]

        self.GAME_TYPE_CODE = info["gameType"]
        self.DATE_ACTIVATED = info["dateActivated"]

        self.STACKED = True if "stacked" in info else False

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} id={self.ID} purchaser={self.PURCHASER_UUID} stacked={self.STACKED}>'
