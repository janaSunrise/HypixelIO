import os
from textwrap import dedent

import hypixelio as hp

# Init the Client
client = hp.Client(api_key=os.environ["HYPIXEL_KEY"])

# Get the guild object
guild = client.get_guild(name="2k")

# Get the essential data
name, ranking, achievements = guild.name, guild.legacy_ranking, guild.achievements

# Print the data
print(
    dedent(
        f"""
    Name: {name}
    ranking: {ranking}
    achievements: {achievements}
    """
    )
)
