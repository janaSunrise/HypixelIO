"""This module is dedicated to definition of the Game count class."""

from .game_count import GameCount


class Games:
    """
    This is the definition of the Custom Hypixel Game count Model.
    """
    def __init__(self, games: dict, player_count: int) -> None:
        """
        Parameters
        ----------
        games: dict
            The Games JSON list data response received from the Hypixel API.
        player_count: int
            The player count in the whole Hypixel Server.
        """
        self.PLAYER_COUNT = player_count

        self.MAIN_LOBBY = GameCount(games["MAIN_LOBBY"])
        self.TOURNAMENT_LOBBY = GameCount(games["TOURNAMENT_LOBBY"])

        self.UHC = GameCount(games["UHC"])
        self.SUPER_SMASH = GameCount(games["SUPER_SMASH"])
        self.LEGACY = GameCount(games["LEGACY"])
        self.BUILD_BATTLE = GameCount(games["BUILD_BATTLE"])
        self.BATTLEGROUND = GameCount(games["BATTLEGROUND"])
        self.WALLS3 = GameCount(games["WALLS3"])
        self.HOUSING = GameCount(games["HOUSING"])
        self.SPEED_UHC = GameCount(games["SPEED_UHC"])
        self.DUELS = GameCount(games["DUELS"])
        self.REPLAY = GameCount(games["REPLAY"])
        self.SURVIVAL_GAMES = GameCount(games["SURVIVAL_GAMES"])
        self.PROTOTYPE = GameCount(games["PROTOTYPE"])
        self.MURDER_MYSTERY = GameCount(games["MURDER_MYSTERY"])
        self.MCGO = GameCount(games["MCGO"])
        self.BEDWARS = GameCount(games["BEDWARS"])
        self.SKYBLOCK = GameCount(games["SKYBLOCK"])
        self.ARCADE = GameCount(games["ARCADE"])
        self.PIT = GameCount(games["PIT"])
        self.TNTGAMES = GameCount(games["TNTGAMES"])
        self.SKYWARS = GameCount(games["SKYWARS"])
        self.LIMBO = GameCount(games["LIMBO"])

        self.IDLE = GameCount(games["IDLE"])
        self.QUEUE = GameCount(games["QUEUE"])

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} lobby={self.MAIN_LOBBY} idle={self.IDLE} queue={self.QUEUE} ' \
               f'players={self.PLAYER_COUNT}>'
