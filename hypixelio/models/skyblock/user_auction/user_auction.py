import typing as t

from hypixelio.models.skyblock.auction import SkyblockAuction


class SkyblockUserAuction:
    def __init__(self, data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The data from the Hypixel API endpoint.
        """
        self.auctions = [SkyblockAuction(auction) for auction in data["auctions"]]

    def __len__(self) -> int:
        return len(self.auctions)

    def __getitem__(self, key: int) -> SkyblockAuction:
        return self.auctions[key]

    def __setitem__(self, key: int, value: SkyblockAuction) -> None:
        self.auctions[key] = value

    def __iter__(self) -> t.Iterator:
        return iter(self.auctions)
