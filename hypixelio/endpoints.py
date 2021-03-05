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
        "find_guild": "/findGuild"
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
