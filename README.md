```
                                        __  __            _           __   ________ 
                                       / / / /_  ______  (_)  _____  / /  /  _/ __ \
                                      / /_/ / / / / __ \/ / |/_/ _ \/ /   / // / / /
                                     / __  / /_/ / /_/ / />  </  __/ /  _/ // /_/ / 
                                    /_/ /_/\__, / .___/_/_/|_|\___/_/  /___/\____/  
                                          /____/_/                                  
```

### A Modern Efficient and Easy way of interacting with the Hypixel API!

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![PyPI - License](https://img.shields.io/pypi/l/HypixelIO)](https://pypi.org/project/HypixelIO)
[![PyPI download month](https://img.shields.io/pypi/dm/ansicolortags.svg)](https://pypi.org/project/HypixelIO/)
[![PyPI](https://img.shields.io/pypi/v/HypixelIO)](https://pypi.org/project/HypixelIO/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/HypixelIO)](https://pypi.org/project/HypixelIO/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/janaSunrise/HypixelIO/graphs/commit-activity)

[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/janaSunrise/HypixelIO)](https://github.com/janaSunrise/HypixelIO)

[![Discord](https://img.shields.io/discord/734712951621025822?style=for-the-badge)](https://discord.gg/6bB3UWj)

## 🚀 Installing
Note: **Python 3.6 or above is required!**
```bash
# Windows
py -3 -m pip install -U HypixelIO

# Linux or MacOS
python3 -m pip install -U HypixelIO

# Install the development version
python3 -m pip install -U git+https://github.com/janaSunrise/HypixelIO
```

## ✌ Usage

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

#### Implementing caching with the Requests.

```python
from hypixelio import Client, Converters, Caching, CacheBackend

config = Caching("cache", CacheBackend.memory, 100, False)

client = Client(api_key="your-api-key", cache=True, cache_config=config)

boosters = client.get_boosters()

print(boosters[0].ID)
```

## ▶ Documentation for the API
API-Help section: [https://hypixel.net/threads/guide-using-the-hypixel-api-with-python.2596749/](https://hypixel.net/threads/guide-using-the-hypixel-api-with-python.2596749/)

## 🤝 Contributing

Contributions, issues and feature requests are welcome. After cloning & setting up project locally, you can just submit a PR to this repo and it will be deployed once it's accepted.

**⚠️ Note - Commit & PR Title :**

It’s good to have descriptive commit messages so that other folks can make sense of what your commit is doing.

Read [conventional commits](https://www.conventionalcommits.org/en/v1.0.0-beta.3/) before making the commit message.

## 🙌 Show your support

Be sure to leave a ⭐️ if you like the project!

## 📢 Changelog
If you're interested in seeing the **Changelog**, Go [here!](https://github.com/janaSunrise/HypixelIO/blob/main/CHANGELOG.md)

Made by janaSunrise with ❤
