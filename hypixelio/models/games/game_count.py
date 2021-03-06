class GameCount:
    """
    This is the definition of the Custom Hypixel API Game Mode Count Model.
    """
    def __init__(self, game: dict) -> None:
        """
        Parameters
        ----------
        game: dict
            The Game JSON data response received from the Hypixel API.
        """
        self.PLAYERS = game["players"]
        self.MODES = game.get("modes")

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} players="{self.PLAYERS}" modes={self.MODES}>'
