class SkyblockAuction:
    def __init__(self, auction_data: dict) -> None:
        """
        Parameters
        ----------
        auction_data: dict
            The auction JSON model to be parsed.
        """
        self.ID = auction_data.get("_id")
        self.UUID = auction_data["uuid"]
        self.AUCTIONEER = auction_data["auctioneer"]

        self.ITEM_NAME = auction_data["item_name"]
        self.ITEM_LORE = auction_data["item_lore"]

        self.CATEGORY = auction_data["category"]
        self.TIER = auction_data["tier"]
        self.STARTING_BID = auction_data["starting_bid"]

        self.CLAIMED_BIDDERS = auction_data.get("claimed_bidders")
        self.BIDS = auction_data.get("bids")
        self.HIGEST_BID = auction_data.get("highest_bid_amount")

    def __str__(self) -> str:
        return self.ID

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} id="{self.ID}" uuid="{self.UUID}">'

    def __hash__(self) -> int:
        return hash(self.ID)

    def __eq__(self, other: "SkyblockAuction") -> bool:
        return self.ID == other.ID
