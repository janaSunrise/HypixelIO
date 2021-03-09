"""This module is dedicated to definition of the Leaderboard class."""

from .leaderboard_data import LeaderboardData as data


class Leaderboard:
    """This is the definition of the Custom Hypixel API Leaderboard Model."""
    def __init__(self, board: dict) -> None:
        """
        Parameters
        ----------
        board: dict
            The Leaderboard JSON data response received from the Hypixel API.
        """
        self.ARENA = [data(arena) for arena in board['ARENA']]
        self.MCGO = [data(arena) for arena in board['MCGO']]
        self.BATTLEGROUND = [data(arena) for arena in board['BATTLEGROUND']]
        self.SURVIVAL_GAMES = [data(arena) for arena in board['SURVIVAL_GAMES']]
        self.UHC = [data(arena) for arena in board['UHC']]
        self.WALLS = [data(arena) for arena in board['WALLS']]
        self.PAINTBALL = [data(arena) for arena in board['PAINTBALL']]
        self.SKYWARS = [data(arena) for arena in board['SKYWARS']]
        self.MURDER_MYSTERY = [data(arena) for arena in board['MURDER_MYSTERY']]
        self.SUPER_SMASH = [data(arena) for arena in board['SUPER_SMASH']]
        self.DUELS = [data(arena) for arena in board['DUELS']]
        self.SPEED_UHC = [data(arena) for arena in board['SPEED_UHC']]
        self.TNTGAMES = [data(arena) for arena in board['TNTGAMES']]
        self.BEDWARS = [data(arena) for arena in board['BEDWARS']]
        self.GINGERBREAD = [data(arena) for arena in board['GINGERBREAD']]
        self.BUILD_BATTLE = [data(arena) for arena in board['BUILD_BATTLE']]
        self.ARCADE = [data(arena) for arena in board['ARCADE']]
        self.SKYCLASH = [data(arena) for arena in board['SKYCLASH']]
        self.QUAKECRAFT = [data(arena) for arena in board['QUAKECRAFT']]
        self.TRUE_COMBAT = [data(arena) for arena in board['TRUE_COMBAT']]
        self.WALLS3 = [data(arena) for arena in board['WALLS3']]
        self.VAMPIREZ = [data(arena) for arena in board['VAMPIREZ']]
