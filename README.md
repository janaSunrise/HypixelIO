```
    __  __            _           __   ________ 
   / / / /_  ______  (_)  _____  / /  /  _/ __ \
  / /_/ / / / / __ \/ / |/_/ _ \/ /   / // / / /
 / __  / /_/ / /_/ / />  </  __/ /  _/ // /_/ / 
/_/ /_/\__, / .___/_/_/|_|\___/_/  /___/\____/  
      /____/_/                                  
```

### A Modern Efficient and Easy way of interacting with the Hypixel API!

### Usage

```python
from hypixelio import Client

client = Client(api_key="your-api-key")

boosters = client.getBoosters()  # Get the boosters object

friends = client.getFriends(uuid="user's-uuid")  # Returns the Friend's object
```

### TODOs PLANNED

- [ ] Implement Games and leaderboard Models in searching
- [ ] Add Examples for using the code in `README.md`
- [x] Add boosters API Section
- [ ] Add Resources API Section
- [ ] Add Skyblock API Section
- [ ] Converters like
      - UUID to Username
      - Username to UUID
- [ ] Implement caching for faster fetching


API-Help section: [https://hypixel.net/threads/guide-using-the-hypixel-api-with-python.2596749/](https://hypixel.net/threads/guide-using-the-hypixel-api-with-python.2596749/)

Made by janaSunrise with ❤
