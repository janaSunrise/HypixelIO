class SkyblockAuction:
    def __init__(self, auction_data: dict) -> None:
        """
        Parameters
        ----------
        auction_data: dict
            The auction JSON model to be parsed.
        """
        self.id = auction_data["_id"]
        self.uuid = auction_data["uuid"]

        self.auctioneer = auction_data["auctioneer"]

        self.item_name = auction_data["item_name"]
        self.item_lore = auction_data["item_lore"]

        self.category = auction_data["category"]
        self.tier = auction_data["tier"]
        self.starting_big = auction_data["starting_bid"]

        self.claimed_bidders = auction_data.get("claimed_bidders")
        self.bids = auction_data.get("bids")
        self.highest_bid = auction_data.get("highest_bid_amount")

    def __str__(self) -> str:
        return self.id

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} id="{self.id}" uuid="{self.uuid}">'

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: "SkyblockAuction") -> bool:
        return self.id == other.id
