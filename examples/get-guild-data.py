from textwrap import dedent

import hypixelio as hp

# Init the Client
client = hp.Client(api_key="your-api-key")

# Get the guild object
guild = client.get_guild(name="2k")

# Get the essential data
name, ranking, achievements = guild.NAME, guild.LEGACY_RANKING, guild.ACHIEVEMENTS

# Print the data
print(
    dedent(f"""
    Name: {name}
    ranking: {ranking}
    achievements: {achievements}
    """)
)
