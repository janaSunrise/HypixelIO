class SkyblockBazaarItem:
    def __init__(self, data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The product data from the Hypixel bazaar API endpoint.
        """
        self.PRODUCT_ID = data["productId"]

        self.SELL_PRICE = data["sellPrice"]
        self.SELL_VOLUME = data["sellVolume"]
        self.SELL_MOVING_WEEK = data["sellMovingWeek"]
        self.SELL_ORDERS = data["sellOrders"]

        self.BUY_PRICE = data["buyPrice"]
        self.BUY_VOLUME = data["buyVolume"]
        self.BUY_MOVING_WEEK = data["buyMovingWeek"]
        self.BUY_ORDERS = data["buyOrders"]

    def __str__(self) -> str:
        return self.PRODUCT_ID

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} id="{self.PRODUCT_ID}" sell_price="{self.SELL_PRICE}" ' \
               f'buy_price="{self.BUY_PRICE}">'

    def __hash__(self) -> int:
        return hash(self.PRODUCT_ID)

    def __eq__(self, other: "SkyblockBazaarItem") -> bool:
        return self.PRODUCT_ID == other.PRODUCT_ID
