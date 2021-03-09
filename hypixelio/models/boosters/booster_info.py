class BoosterInfo:
    """The Hypixel API Booster's Info Model."""
    def __init__(self, info: dict) -> None:
        """
        Parameters
        ----------
        info: dict
            This contains the Returned JSON Response for the Booster's List Element API Request.
        """
        self.ID = info["_id"]
        self.PURCHASER_UUID = info["purchaserUuid"]

        self.AMOUNT = info["amount"]
        self.ORIGINAL_LENGTH = info["originalLength"]
        self.LENGTH = info["length"]

        self.GAME_TYPE_CODE = info["gameType"]
        self.DATE_ACTIVATED = info["dateActivated"]

        self.STACKED = "stacked" in info

    def __eq__(self, other: "BoosterInfo") -> bool:
        return self.ID == other.ID and self.PURCHASER_UUID == other.PURCHASER_UUID

    def __hash__(self) -> int:
        return hash((self.ID, self.PURCHASER_UUID))

    def __str__(self) -> str:
        return self.PURCHASER_UUID

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} id="{self.ID}" purchaser="{self.PURCHASER_UUID}" stacked={self.STACKED}>'
