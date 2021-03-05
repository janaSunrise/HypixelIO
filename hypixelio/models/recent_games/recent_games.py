import typing as t

from .recent_game_info import RecentGameInfo


class RecentGames:
    def __init__(self, data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The JSON data received from the Hypixel API.
        """
        self.UUID = data["uuid"]
        self.GAMES = [RecentGameInfo(game) for game in data["games"]]

    def __len__(self) -> int:
        return len(self.GAMES)

    def __getitem__(self, key: int) -> RecentGameInfo:
        return self.GAMES[key]

    def __setitem__(self, key: int, value: RecentGameInfo) -> None:
        self.GAMES[key] = value

    def __iter__(self) -> t.Iterator:
        return iter(self.GAMES)

    def __str__(self) -> str:
        return self.UUID

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} uuid="{self.UUID}">'

    def __hash__(self) -> int:
        return hash(self.UUID)

    def __eq__(self, other: "RecentGames") -> bool:
        return self.UUID == other.UUID
