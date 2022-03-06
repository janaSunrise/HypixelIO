class SkyblockBazaarItem:
    def __init__(self, data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The product data from the Hypixel bazaar API endpoint.
        """
        self.product_id = data["productId"]

        self.sell_price = data["sellPrice"]
        self.sell_volume = data["sellVolume"]
        self.sell_moving_week = data["sellMovingWeek"]
        self.sell_orders = data["sellOrders"]

        self.buy_price = data["buyPrice"]
        self.buy_volume = data["buyVolume"]
        self.buy_moving_week = data["buyMovingWeek"]
        self.buy_orders = data["buyOrders"]

    def __str__(self) -> str:
        return self.product_id

    def __repr__(self) -> str:
        return (
            f'<{self.__class__.__name__} id="{self.product_id}" sell_price="{self.sell_price}" '
            f'buy_price="{self.buy_price}">'
        )

    def __hash__(self) -> int:
        return hash(self.product_id)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SkyblockBazaarItem):
            return False
        return self.product_id == other.product_id
