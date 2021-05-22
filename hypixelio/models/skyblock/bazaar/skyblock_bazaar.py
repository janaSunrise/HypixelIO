from .bazaar_item import SkyblockBazaarItem


class SkyblockBazaar:
    def __init__(self, data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The data from the Hypixel API endpoint.
        """
        self.PRODUCTS = {}

        for key, value in data["products"].items():
            bazaar_item_object = SkyblockBazaarItem(value["quick_status"])
            self.PRODUCTS[key] = bazaar_item_object
