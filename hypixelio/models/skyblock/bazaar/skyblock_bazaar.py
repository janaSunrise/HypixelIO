from .bazaar_item import SkyblockBazaarItem


class SkyblockBazaar:
    def __init__(self, data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The data from the Hypixel API endpoint.
        """
        self.__PRODUCTS = data["products"]

        for key, value in self.__PRODUCTS.items():
            bazaar_item_object = SkyblockBazaarItem(value["quick_status"])
            setattr(self, key, bazaar_item_object)
