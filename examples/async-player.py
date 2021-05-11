import os
from textwrap import dedent

from hypixelio.ext.asyncio import AsyncClient


async def fetch() -> None:
    # Login to the API
    client = AsyncClient(api_key=os.environ["HYPIXEL_KEY"])

    # Get a player object
    player = await client.get_player(name="janaSunrise")

    # Extract the data from the object
    name, uuid, achievements = player.NAME, player.UUID, player.ACHIEVEMENTS

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
