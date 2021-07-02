import os

from hypixelio import Client

# Initialize the Client
# Enable cache, and leave config to memory, default one.
client = Client(api_key=os.environ["HYPIXEL_KEY"], cache=True)

# Get the boosters
boosters = client.get_boosters()

print(boosters[0].ID)
