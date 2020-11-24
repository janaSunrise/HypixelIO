import os

from hypixelio import CacheBackend, Caching, Client

# Configure the caching
config = Caching("cache", CacheBackend.memory, 100, False)

# Initialize the Client
client = Client(api_key=os.environ["HYPIXEL_KEY"], cache=True, cache_config=config)

# Get the boosters
boosters = client.get_boosters()

print(boosters[0].ID)
