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
        self.FAIRY_SOULS_COLLECTED = member_data.get("fairy_souls_collected")
        self.FISHING_TREASURE_COUNT = member_data.get("fishing_treasure_caught")

        self.STATS = member_data["stats"]
        self.OBJECTIVES = member_data["objectives"]

        self.CRAFTED_GENERATORS = member_data.get("crafted_generators")
        self.VISITED_ZONES = member_data.get("visited_zones")
        self.ACHIEVEMENT_SPAWNED_ISLAND_TYPES = member_data.get("achievement_spawned_island_types")

        self.SLAYER_QUEST = member_data.get("slayer_quest")
        self.SLAYER_BOSSES = member_data.get("slayer_bosses")

        self.PETS = member_data["pets"]
        self.GRIFFIN = member_data["griffin"]

        self.UNLOCKED_COLLECTION_TIERS = member_data.get("unlocked_coll_tiers")

        self.SKILLS = {
            "alchemy": member_data.get("experience_skill_alchemy"),
            "farming": member_data.get("experience_skill_farming"),
            "taming": member_data.get("experience_skill_taming"),
            "enchanting": member_data.get("experience_skill_enchanting"),
            "fishing": member_data.get("experience_skill_fishing"),
            "foraging": member_data.get("experience_skill_foraging"),
            "carpentry": member_data.get("experience_skill_carpentry"),
            "runecrafting": member_data.get("experience_skill_runecrafting"),
            "combat": member_data.get("experience_skill_combat"),
            "mining": member_data.get("experience_skill_mining")
        }

        self.COLLECTION = member_data.get("collection")
