from .leaderboard_data import LeaderboardData


class Leaderboard:
    """This is the definition of the Custom Hypixel API Leaderboard Model."""

    def __init__(self, board: dict) -> None:
        """
        Parameters
        ----------
        board: dict
            The Leaderboard JSON data response received from the Hypixel API.
        """
        self.ARENA = [LeaderboardData(arena) for arena in board["ARENA"]]
        self.MCGO = [LeaderboardData(arena) for arena in board["MCGO"]]
        self.BATTLEGROUND = [LeaderboardData(arena) for arena in board["BATTLEGROUND"]]
        self.SURVIVAL_GAMES = [LeaderboardData(arena) for arena in board["SURVIVAL_GAMES"]]
        self.UHC = [LeaderboardData(arena) for arena in board["UHC"]]
        self.WALLS = [LeaderboardData(arena) for arena in board["WALLS"]]
        self.PAINTBALL = [LeaderboardData(arena) for arena in board["PAINTBALL"]]
        self.SKYWARS = [LeaderboardData(arena) for arena in board["SKYWARS"]]
        self.MURDER_MYSTERY = [LeaderboardData(arena) for arena in board["MURDER_MYSTERY"]]
        self.SUPER_SMASH = [LeaderboardData(arena) for arena in board["SUPER_SMASH"]]
        self.DUELS = [LeaderboardData(arena) for arena in board["DUELS"]]
        self.SPEED_UHC = [LeaderboardData(arena) for arena in board["SPEED_UHC"]]
        self.TNTGAMES = [LeaderboardData(arena) for arena in board["TNTGAMES"]]
        self.BEDWARS = [LeaderboardData(arena) for arena in board["BEDWARS"]]
        self.GINGERBREAD = [LeaderboardData(arena) for arena in board["GINGERBREAD"]]
        self.BUILD_BATTLE = [LeaderboardData(arena) for arena in board["BUILD_BATTLE"]]
        self.ARCADE = [LeaderboardData(arena) for arena in board["ARCADE"]]
        self.SKYCLASH = [LeaderboardData(arena) for arena in board["SKYCLASH"]]
        self.QUAKECRAFT = [LeaderboardData(arena) for arena in board["QUAKECRAFT"]]
        self.TRUE_COMBAT = [LeaderboardData(arena) for arena in board["TRUE_COMBAT"]]
        self.WALLS3 = [LeaderboardData(arena) for arena in board["WALLS3"]]
        self.VAMPIREZ = [LeaderboardData(arena) for arena in board["VAMPIREZ"]]
