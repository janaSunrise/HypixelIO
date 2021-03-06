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
        self.FAIRY_SOULS_COLLECTED = member_data["fairy_souls_collected"]
        self.FISHING_TREASURE_COUNT = member_data["fishing_treasure_caught"]

        self.STATS = member_data["stats"]
        self.OBJECTIVES = member_data["objectives"]

        self.CRAFTED_GENERATORS = member_data["crafted_generators"]
        self.VISITED_ZONES = member_data["visited_zones"]
        self.ACHIEVEMENT_SPAWNED_ISLAND_TYPES = member_data["achievement_spawned_island_types"]

        self.SLAYER_QUEST = member_data["slayer_quest"]
        self.SLAYER_BOSSES = member_data["slayer_bosses"]

        self.PETS = member_data["pets"]
        self.GRIFFIN = member_data["griffin"]

        self.UNLOCKED_COLLECTION_TIERS = member_data["unlocked_coll_tiers"]

        self.SKILLS = {
            "alchemy": member_data["experience_skill_alchemy"],
            "farming": member_data["experience_skill_farming"],
            "taming": member_data["experience_skill_taming"],
            "enchanting": member_data["experience_skill_enchanting"],
            "fishing": member_data["experience_skill_fishing"],
            "foraging": member_data["experience_skill_foraging"],
            "carpentry": member_data["experience_skill_carpentry"]
        }

        self.COLLECTION = member_data["collection"]
