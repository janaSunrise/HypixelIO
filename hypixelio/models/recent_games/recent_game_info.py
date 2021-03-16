class RecentGameInfo:
    def __init__(self, game: dict) -> None:
        """
        Parameters
        ----------
        game: dict
            The game's JSON data received from the Hypixel API.
        """
        self.DATE = game["date"]
        self.END_DATETIME = game["ended"]

        self.GAME_TYPE = game["gameType"]
        self.MODE = game.get("mode")
        self.MAP = game["map"]

    def __hash__(self) -> int:
        return hash((self.DATE, self.MAP))

    def __str__(self) -> str:
        return self.GAME_TYPE

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} game_type="{self.GAME_TYPE}" mode="{self.MODE}" map="{self.MAP}">'
