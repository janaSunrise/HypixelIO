import os
from textwrap import dedent

import hypixelio as hp

# Login to the API
client = hp.Client(api_key=os.environ["HYPIXEL_KEY"])

# Get a player object
player = client.get_player(name="janaSunrise")

# Extract the data from the object
name, uuid, achievements = player.name, player.uuid, player.achievements

# Print the data
print(
    dedent(
        f"""
    Name: {name}
    UUID: {uuid}
    Achievements: {achievements}
    """
    )
)
