class SkyblockProfileMember:
    def __init__(self, member_data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The JSON data received from the Hypixel API.
        """
        self.coin_purse = member_data["coin_purse"]
        self.death_count = member_data["death_count"]
        self.fairy_souls_collected = member_data.get("fairy_souls_collected")
        self.fishing_treasure_count = member_data.get("fishing_treasure_caught")

        self.stats = member_data["stats"]
        self.objectives = member_data["objectives"]

        self.crafted_generators = member_data.get("crafted_generators")
        self.visited_zones = member_data.get("visited_zones")
        self.achievement_spawned_island_types = member_data.get(
            "achievement_spawned_island_types"
        )

        self.slayer_quest = member_data.get("slayer_quest")
        self.slayer_bosses = member_data.get("slayer_bosses")

        self.pets = member_data["pets"]
        self.griffin = member_data["griffin"]

        self.unlocked_collection_tiers = member_data.get("unlocked_coll_tiers")

        self.skills = {
            "alchemy": member_data.get("experience_skill_alchemy"),
            "farming": member_data.get("experience_skill_farming"),
            "taming": member_data.get("experience_skill_taming"),
            "enchanting": member_data.get("experience_skill_enchanting"),
            "fishing": member_data.get("experience_skill_fishing"),
            "foraging": member_data.get("experience_skill_foraging"),
            "carpentry": member_data.get("experience_skill_carpentry"),
            "runecrafting": member_data.get("experience_skill_runecrafting"),
            "combat": member_data.get("experience_skill_combat"),
            "mining": member_data.get("experience_skill_mining"),
        }

        self.collection = member_data.get("collection")
