import typing as t

from hypixelio.models.skyblock.auction import SkyblockAuction


class SkyblockActiveAuction:
    def __init__(self, data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The data from the Hypixel API endpoint.
        """
        self.PAGE_NUMBER = data["page"]
        self.TOTAL_PAGES = data["totalPages"]
        self.TOTAL_AUCTION = data["totalAuctions"]
        self.AUCTIONS = [SkyblockAuction(auction) for auction in data["auctions"]]

    def __len__(self) -> int:
        return len(self.AUCTIONS)

    def __getitem__(self, key: int) -> SkyblockAuction:
        return self.AUCTIONS[key]

    def __setitem__(self, key: int, value: SkyblockAuction) -> None:
        self.AUCTIONS[key] = value

    def __iter__(self) -> t.Iterator:
        return iter(self.AUCTIONS)
