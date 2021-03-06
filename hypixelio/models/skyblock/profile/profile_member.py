class SkyblockProfileMember:
    def __init__(self, member_data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The JSON data received from the Hypixel API.
        """
        self.COIN_PURSE = member_data["coin_purse"]
        self.DEATH_COUNT = member_data["death_count"]

        self.STATS = member_data["stats"]
        self.OBJECTIVES = member_data["objectives"]

        self.CRAFTED_GENERATORS = member_data["crafted_generators"]
