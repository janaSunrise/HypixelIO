```
                      __  __            _           __   ________
                     / / / /_  ______  (_)  _____  / /  /  _/ __ \
                    / /_/ / / / / __ \/ / |/_/ _ \/ /   / // / / /
                   / __  / /_/ / /_/ / />  </  __/ /  _/ // /_/ /
                  /_/ /_/\__, / .___/_/_/|_|\___/_/  /___/\____/
                        /____/_/
```

<h1 align="center">HypixelIO</h1>

<h3 align="center">A Modern, Efficient and Easy way of interacting with the Hypixel API!</h3>

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

<a href="https://discord.gg/MKC4qna4Gz">
    <img src="https://discordapp.com/api/guilds/835940276869791816/widget.png?style=shield" alt="Discord" />
</a>

</p>

<!-- Links -->
<h3 align="center">
  <a href="https://hypixelio.readthedocs.org">Docs</a>
  <span> · </span>
  <a href="https://github.com/janaSunrise/HypixelIO/issues">Report a bug</a>
  <span> · </span>
  <a href="https://github.com/janaSunrise/HypixelIO/discussions">Discussions</a>
  <span> · </span>
  <a href="https://discord.gg/MKC4qna4Gz">Discord</a>
</h3>

## ✨ Why choose HypixelIO?

- Modern way of handling requests
- Modern OOP based structure
- Both Async and blocking support
- Simple ratelimit handling and caching
- Elegant design with complete optimization
- Easy to use with a modern and simple design
- Complete API coverage

## 🚀 Installing

**Python 3.7 or above is required!**

```sh
# Windows
py -3 -m pip install -U HypixelIO

# Linux or MacOS
python3 -m pip install -U HypixelIO

# Install the nightly build
python3 -m pip install -U git+https://github.com/janaSunrise/HypixelIO
```

You can also get extra features with this library. Here's how:

```sh
# Use [speedups] to speed up only for async API
python3 -m pip install -U "HypixelIO[speedups]"
```

## Usage

```python
from hypixelio import Client, Converters

client = Client(api_key="your-api-key")

boosters = client.get_boosters()  # Get the boosters object

friends = client.get_friends(uuid="user's-uuid")  # Returns the Friends object
# Or, if you don't know the UUID
friends = client.get_friends(name="user's-username")

print(boosters[0].id)
print(friends.friends[0].receiver_id)
```

### Async API usage

```python
import asyncio

from hypixelio import AsyncClient, AsyncConverters

client = AsyncClient(api_key="your-api-key")

# Async function to fetch info
async def fetch_from_hypixel():
    boosters = await client.get_boosters()  # Get the boosters object

    friends = await client.get_friends(uuid="user's-uuid")  # Returns the Friends object
    # Or, if you don't know the UUID
    friends = await client.get_friends(name="user's-username")

    # Safely close the connection
    await client.close()

    return boosters, friends

# Run the coroutine using `asyncio`
boosters, friends = asyncio.run(fetch_from_hypixel())

print(boosters[0].id)
print(friends.friends[0].receiver_id)
```

**Find more examples [here](https://github.com/janaSunrise/HypixelIO/tree/main/examples)!**

## 📢 Changelog

If you're interested in seeing the **Changelog**, Go [here!](https://github.com/janaSunrise/HypixelIO/blob/main/CHANGELOG.md)

## 🤝 Contributing

Contributions, issues and feature requests are welcome. After cloning & setting up project locally, you can just submit
a PR to this repo and it will be deployed once it's accepted.

⚠️ It’s good to have descriptive commit messages, or PR titles so that other contributors can understand about your
commit or the PR Created. Read [conventional commits](https://www.conventionalcommits.org/en/v1.0.0-beta.3/) before
making the commit message. You can find our contributing guidelines
[here](https://github.com/janaSunrise/HypixelIO/blob/main/CONTRIBUTING.md)

We have a branch called `dev` containing development code. If you're contributing, Remember to contribute to
`dev` branch, instead of `main`.

## 💬 Get in touch

If you have various suggestions, questions or want to discuss things with our community, Have a look at
[Github discussions](https://github.com/janaSunrise/HypixelIO/discussions) or join our Discord server!

[![Discord](https://discordapp.com/api/guilds/835940276869791816/widget.png?style=shield)](https://discord.gg/MKC4qna4Gz)

## 👋 Show your support

Be sure to drop a 🌟 if you like the project!

## ▶ Links

- [Official Documentation](http://hypixelio.rtfd.io/)
- [Raise an Issue](https://github.com/janaSunrise/HypixelIO/issues)
- [Discussions](https://github.com/janaSunrise/HypixelIO/discussions)
- [Hypixel API Documentation](https://api.hypixel.net)

<div align="center">Made by Sunrit Jana with ❤</div>
