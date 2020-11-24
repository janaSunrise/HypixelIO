```
                      __  __            _           __   ________ 
                     / / / /_  ______  (_)  _____  / /  /  _/ __ \
                    / /_/ / / / / __ \/ / |/_/ _ \/ /   / // / / /
                   / __  / /_/ / /_/ / />  </  __/ /  _/ // /_/ / 
                  /_/ /_/\__, / .___/_/_/|_|\___/_/  /___/\____/  
                        /____/_/                                     
```

<h3 align="center">

### A Modern Efficient and Easy way of interacting with the Hypixel API!

</p>

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

</p>

<p align="center">

<a href="https://discord.gg/6bB3UWj">
    <img src="https://img.shields.io/discord/734712951621025822?style=for-the-badge" alt="Discord server" />
</a>

</p>

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

**Find more examples [here](https://github.com/janaSunrise/HypixelIO/tree/main/examples)**

## 🤝 Contributing

Contributions, issues and feature requests are welcome. After cloning & setting up project locally, you can just submit a PR to this repo and it will be deployed once it's accepted.

⚠️ It’s good to have descriptive commit messages, or PR titles so that other contributors can understand about your commit or the PR Created.
Read [conventional commits](https://www.conventionalcommits.org/en/v1.0.0-beta.3/) before making the commit message.

And, Also we have a Branch named `dev`, So if you're interested in contributing, Please contribute to that branch instead of the `main` branch.

## 📢 Changelog
If you're interested in seeing the **Changelog**, Go [here!](https://github.com/janaSunrise/HypixelIO/blob/main/CHANGELOG.md)

## 🙌 Show your support

Be sure to leave a ⭐️ if you like the project!

## ▶ Links
- API-Help section: [https://hypixel.net/threads/guide-using-the-hypixel-api-with-python.2596749/](https://hypixel.net/threads/guide-using-the-hypixel-api-with-python.2596749/)
- [Raise an Issue](https://github.com/janaSunrise/HypixelIO/issues)


<p align="center">

Made by janaSunrise with ❤

</p>
