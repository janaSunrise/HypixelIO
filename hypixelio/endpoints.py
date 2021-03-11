"""List of all the various endpoint paths."""

API_PATH = {
    "HYPIXEL": {
        "api_key": "/key",
        "boosters": "/boosters",
        "player": "/player",
        "friends": "/friends",
        "watchdog": "/watchdogstats",
        "guild": "/guild",
        "game_info": "/gameCounts",
        "leaderboards": "/leaderboards",
        "find_guild": "/findGuild",
        "status": "/status",
        "recent_games": "/recentgames",
        "skyblock_auctions": "/skyblock/auction",
        "skyblock_active_auctions": "/skyblock/auctions",
        "skyblock_bazaar": "/skyblock/bazaar",
        "skyblock_profile": "/skyblock/profile",
        "achievements": "/resources/achievements",
        "challenges": "/resources/challenges",
        "quests": "/resources/quests",
        "guild_achievements": "/resources/guilds/achievements"
    },
    "MOJANG": {
        "username_to_uuid": "/users/profiles/minecraft/{}",
        "uuid_to_username": "/user/profiles/{}/names",
        "name_history": "/user/profiles/{}/names",
    },
    "CRAFATAR": {
        "avatar": "/avatars/{}",
        "head": "/renders/head/{}",
        "body": "/renders/body/{}",
        "skins": "/skins/{}"
    }
}
