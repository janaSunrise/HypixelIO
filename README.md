```
                      __  __            _           __   ________ 
                     / / / /_  ______  (_)  _____  / /  /  _/ __ \
                    / /_/ / / / / __ \/ / |/_/ _ \/ /   / // / / /
                   / __  / /_/ / /_/ / />  </  __/ /  _/ // /_/ / 
                  /_/ /_/\__, / .___/_/_/|_|\___/_/  /___/\____/  
                        /____/_/                                     
```

<h3 align="center">

<h1 align="center">
  HypixelIO
</h1>

<h3 align="center">
A Modern Efficient and Easy way of interacting with the Hypixel API!
</h3>

</h3>

<p align="center">

<a href="https://www.python.org/">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" alt="Made with Python" />
</a>

</p>

<p align="center">

<a href="https://pypi.org/project/HypixelIO">
    <img src="https://img.shields.io/pypi/l/HypixelIO" alt="PYPI - License" />
</a>

<a href="https://pypi.org/project/HypixelIO">
    <img src="https://img.shields.io/pypi/dm/ansicolortags.svg" alt="PYPI Download per Month" />
</a>

<a href="https://pypi.org/project/HypixelIO">
    <img src="https://img.shields.io/pypi/v/HypixelIO" alt="PYPI" />
</a>

<a href="https://github.com/janaSunrise/HypixelIO/releases">
    <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/janaSunrise/HypixelIO">
  </a>

<a href="https://pypi.org/project/HypixelIO">
    <img src="https://img.shields.io/pypi/pyversions/HypixelIO" alt="PYPI Python Version" />
</a>

<a href="https://GitHub.com/janaSunrise/HypixelIO/graphs/commit-activity">
    <img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" alt="Maintenance" />
</a>

</p>

<p align="center">

<a href="https://github.com/janaSunrise/HypixelIO">
    <img src="https://img.shields.io/github/languages/code-size/janaSunrise/HypixelIO" alt="Code Size" />
</a>

<a href="https://discord.gg/cSC5ZZwYGQ">
    <img src="https://discordapp.com/api/guilds/695008516590534758/widget.png?style=shield" alt="Discord" />
</a>

</p>

<h3 align="center">
  <a href="https://hypixelio.readthedocs.org">Docs</a>
  <span> · </span>
  <a href="https://github.com/janaSunrise/HypixelIO/issues">Report a bug</a>
  <span> · </span>
  <a href="https://github.com/janaSunrise/HypixelIO/discussions">Discussions</a>
  <span> · </span>
  <a href="https://discord.gg/cSC5ZZwYGQ">Discord</a>
</h3>

## ✨ Why choose HypixelIO over others?

- Modern way of handling requests
- Both async and sync support.
- Simple rate handling, and caching.
- Speed optimized
- Easy to use with a modern and simple design
- Full API coverage

## 🚀 Installing
Note: **Python 3.7 or above is required!**
```bash
# Windows
py -3 -m pip install -U HypixelIO

# Linux or MacOS
python3 -m pip install -U HypixelIO

# Install the nightly build
python3 -m pip install -U git+https://github.com/janaSunrise/HypixelIO

# Or use [speedups] to speed up only for async features
python3 -m pip install -U "HypixelIO[speedups]"
```

## Usage

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

### Need async support? We already do!

```python
from hypixelio.ext.asyncio import AsyncClient, AsyncConverters

client = AsyncClient(api_key="your-api-key")

boosters = await client.get_boosters()  # Get the boosters object

friends = await client.get_friends(uuid="user's-uuid")  # Returns the Friends object
# or if you don't know the UUID
friends = await client.get_friends(uuid=Converters.username_to_uuid("your-username"))

print(boosters[0].ID)
print(friends.FRIENDS[0].RECEIVER_ID)
```

**Find more examples [here](https://github.com/janaSunrise/HypixelIO/tree/main/examples)**

## 🤝 Contributing

Contributions, issues and feature requests are welcome. After cloning & setting up project locally, you can just submit 
a PR to this repo and it will be deployed once it's accepted.

⚠️ It’s good to have descriptive commit messages, or PR titles so that other contributors can understand about your 
commit or the PR Created. Read [conventional commits](https://www.conventionalcommits.org/en/v1.0.0-beta.3/) before 
making the commit message.

And, Also we have a branch named `dev`, So if you're interested in contributing, Please contribute to that branch 
instead of the `main` branch.

## 💬 Get in touch

If you have various suggestions, questions or want to discuss things wit our community, Have a look at
[Github discussions](https://github.com/janaSunrise/HypixelIO/discussions) or join our discord server!

[![Discord](https://discordapp.com/api/guilds/695008516590534758/widget.png?style=shield)](https://discord.gg/cSC5ZZwYGQ)


## 📢 Changelog
If you're interested in seeing the **Changelog**, Go [here!](https://github.com/janaSunrise/HypixelIO/blob/main/CHANGELOG.md)

## 🙌 Show your support

Be sure to leave a ⭐️ if you like the project!

## ▶ Links
- [Official Documentation](http://hypixelio.rtfd.io/)
- [Raise an Issue](https://github.com/janaSunrise/HypixelIO/issues)
- API-Help section: [https://hypixel.net/threads/guide-using-the-hypixel-api-with-python.2596749/](https://hypixel.net/threads/guide-using-the-hypixel-api-with-python.2596749/)


<p align="center">

Made by janaSunrise with ❤

</p>
