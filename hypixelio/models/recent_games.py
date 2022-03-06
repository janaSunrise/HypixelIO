import typing as t

from hypixelio.utils import unix_time_to_datetime


class RecentGameInfo:
    def __init__(self, game: dict) -> None:
        """
        Parameters
        ----------
        game: dict
            The game's JSON data received from the Hypixel API.
        """
        self.date = unix_time_to_datetime(game["date"])
        self.end_datetime = unix_time_to_datetime(game["ended"])

        self.game_type = game["gameType"]
        self.mode = game.get("mode")
        self.map = game["map"]

    def __hash__(self) -> int:
        return hash((self.date, self.map))

    def __str__(self) -> str:
        return self.game_type

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} game_type="{self.game_type}" mode="{self.mode}" map="{self.map}">'


class RecentGames:
    def __init__(self, data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The JSON data received from the Hypixel API.
        """
        self.uuid = data["uuid"]
        self.games = [RecentGameInfo(game) for game in data["games"]]

    # Length of the list
    def __len__(self) -> int:
        return len(self.games)

    # Get items
    def __getitem__(self, key: int) -> RecentGameInfo:
        return self.games[key]

    def __setitem__(self, key: int, value: RecentGameInfo) -> None:
        self.games[key] = value

    # Looping
    def __iter__(self) -> t.Iterator:
        return iter(self.games)

    # Other dunder methods
    def __str__(self) -> str:
        return self.uuid

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} uuid="{self.uuid}">'

    def __hash__(self) -> int:
        return hash(self.uuid)

    def __eq__(self, other: "RecentGames") -> bool:
        return self.uuid == other.uuid
