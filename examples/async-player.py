import asyncio
import os
from textwrap import dedent

from hypixelio import AsyncClient


async def fetch() -> None:
    # Login to the API
    client = AsyncClient(api_key=os.environ["HYPIXEL_KEY"])

    # Get a player object
    player = await client.get_player(name="janaSunrise")

    # Close the session
    await client.close()

    # Extract the data from the object
    name, uuid, achievements = player.name, player.uuid, player.achievements

    # Print the data
    print(
        dedent(f"""
        Name: {name}
        UUID: {uuid}
        Achievements: {achievements}
        """)
    )

asyncio.run(fetch())
