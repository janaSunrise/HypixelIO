"""
This module is for defining the constant variables which will be
used all over the code, hence reusing the same things, Instead of
redefining, and accessing from a single place.
"""
__all__ = (
    "HYPIXEL_API",
    "MOJANG_API",
    "RANKS",
    "RANK_COLORS",
    "BEDWARS_PRESTIGE_COLOR",
    "BEDWARS_PRESTIGE_RANKS",
    "GUILD_COLORS__TAG",
    "SKYWARS_PRESTIGES_RANKS",
    "SKYWARS_PRESTIGE_COLOR",
)

HYPIXEL_API = "https://api.hypixel.net"
MOJANG_API = "https://api.mojang.com"

TIMEOUT = 10

RANKS = {
    "NONE": None,
    "VIP": "VIP",
    "VIP_PLUS": "VIP+",
    "MVP": "MVP",
    "MVP_PLUS": "MVP+",
    "SUPERSTAR": "MVP++",
    "YOUTUBER": "YOUTUBE",
    "PIG+++": "PIG+++",
    "BUILD TEAM": "BUILD TEAM",
    "HELPER": "HELPER",
    "MODERATOR": "MOD",
    "ADMIN": "ADMIN",
    "SLOTH": "SLOTH",
    "OWNER": "OWNER"
}

RANK_COLORS = {
    "VIP": int("55FF55", 16),
    "VIP+": int("55FF55", 16),
    "MVP": int("55FFFF", 16),
    "MVP+": int("55FFFF", 16),
    "MVP++": int("FFAA00", 16),
    "YOUTUBE": int("FF5555", 16),
    "PIG+++": int("FF69DC", 16),
    "BUILD TEAM": int("00AAAA", 16),
    "EVENTS": int("FFAA00", 16),
    "HELPER": int("5555FF", 16),
    "MOD": int("00AA00", 16),
    "ADMIN": int("AA0000", 16),
    "SLOTH": int("AA0000", 16),
    "OWNER": int("AA0000", 16),
    None: int("607D8B", 16)
}

BEDWARS_PRESTIGE_RANKS = (
    "Stone",
    "Iron",
    "Gold",
    "Diamond",
    "Emerald",
    "Sapphire",
    "Ruby",
    "Crystal",
    "Opal",
    "Amethyst",
    "Rainbow",
    "Iron Prime",
    "Gold Prime",
    "Diamond Prime",
    "Emerald Prime",
    "Sapphire Prime",
    "Ruby Prime",
    "Crystal Prime",
    "Opal Prime",
    "Amethyst Prime",
    "Mirror",
    "Light",
    "Dawn",
    "Dusk",
    "Air",
    "Wind",
    "Nebula",
    "Thunder",
    "Earth",
    "Water",
    "Fire"
)

SKYWARS_PRESTIGES_RANKS = (
    "Stone",
    "Iron",
    "Gold",
    "Diamond",
    "Emerald",
    "Sapphire",
    "Ruby",
    "Crystal",
    "Opal",
    "Amethyst",
    "Rainbow",
    "Mystic"
)

BEDWARS_PRESTIGE_COLOR = (
    int("607D8B", 16),
    int("95A5A6", 16),
    int("FFAC0F", 16),
    int("55FFFF", 16),
    int("00AA00", 16),
    int("00AAAA", 16),
    int("AA0000", 16),
    int("FF69DC", 16),
    int("2562E9", 16),
    int("AA00AA", 16),
    int("1ABC9C", 16),
    int("607D8B", 16),
    int("95A5A6", 16),
    int("FFAC0F", 16),
    int("55FFFF", 16),
    int("00AA00", 16),
    int("00AAAA", 16),
    int("AA0000", 16),
    int("FF69DC", 16),
    int("2562E9", 16),
    int("AA00AA", 16)
)

SKYWARS_PRESTIGE_COLOR = (
    int("607D8B", 16),
    int("95A5A6", 16),
    int("FFAC0F", 16),
    int("55FFFF", 16),
    int("00AA00", 16),
    int("00AAAA", 16),
    int("AA0000", 16),
    int("FF69DC", 16),
    int("2562E9", 16),
    int("AA00AA", 16),
    int("AA00AA", 16)
)

GUILD_COLORS__TAG = {
    "GRAY": int("607D8B", 16),
    "GOLD": int("FFAC0F", 16),
    "DARK_AQUA": int("00AAAA", 16),
    "DARK_GREEN": int("00AA00", 16),
    "YELLOW": int("FFFF55", 16)
}
