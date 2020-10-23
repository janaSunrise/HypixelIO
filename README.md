```
    __  __            _           __   ________ 
   / / / /_  ______  (_)  _____  / /  /  _/ __ \
  / /_/ / / / / __ \/ / |/_/ _ \/ /   / // / / /
 / __  / /_/ / /_/ / />  </  __/ /  _/ // /_/ / 
/_/ /_/\__, / .___/_/_/|_|\___/_/  /___/\____/  
      /____/_/                                  
```

### A Modern Efficient and Easy way of interacting with the Hypixel API!

### Installing
Note: **Python 3.6 or above is required!**
```bash
# Windows
py -3 -m pip install -U HypixelIO

# Linux or MacOS
python3 -m pip install -U HypixelIO

# Install the development version
python3 -m pip install -U git+https://github.com/janaSunrise/HypixelIO
```

### Usage

```python
from hypixelio import Client, Converters

client = Client(api_key="your-api-key")

boosters = client.get_boosters()  # Get the boosters object

friends = client.get_friends(uuid="user's-uuid")  # Returns the Friends object
# or if you don't know the UUID
friends = client.get_friends(uuid=Converters.username_to_uuid("your-username"))

print(boosters[0].ID)
print(friends.FRIENDS[0].RECEIVER_ID)
```

### TODOs PLANNED

- [x] Implement Games and leaderboard Models in searching
- [x] Add Examples for using the code in `README.md`
- [x] Add boosters API Section
- [ ] Add Resources API Section
- [ ] Add Skyblock API Section
- [x] Add Find guild API Section
- [x] Converters like
      - UUID to Username
      - Username to UUID
- [x] Fix `__repr__` and `__str__`
- [x] Implement caching for efficiency

If you're interested in seeing the **Changelog**, Go [here!](https://github.com/janaSunrise/HypixelIO/blob/main/CHANGELOG.md)

API-Help section: [https://hypixel.net/threads/guide-using-the-hypixel-api-with-python.2596749/](https://hypixel.net/threads/guide-using-the-hypixel-api-with-python.2596749/)

Made by janaSunrise with ❤
