class LeaderboardData:
    def __init__(self, data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The Leaderboard JSON data per game response received from the Hypixel API.
        """
        self.path = data["path"]
        self.prefix = data["prefix"]

        self.title = data["title"]

        self.location = data["location"]
        self.count = data["count"]

        self.leaders_uuid = data["leaders"]

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} title="{self.title}" location="{self.location}">'

    def __str__(self) -> str:
        return self.title


class Leaderboard:
    def __init__(self, board: dict) -> None:
        """
        Parameters
        ----------
        board: dict
            The Leaderboard JSON data response received from the Hypixel API.
        """
        self.arena = [LeaderboardData(arena) for arena in board["ARENA"]]
        self.mcgo = [LeaderboardData(arena) for arena in board["MCGO"]]
        self.battleground = [LeaderboardData(arena) for arena in board["BATTLEGROUND"]]
        self.survival_games = [
            LeaderboardData(arena) for arena in board["SURVIVAL_GAMES"]
        ]
        self.uhc = [LeaderboardData(arena) for arena in board["UHC"]]
        self.walls = [LeaderboardData(arena) for arena in board["WALLS"]]
        self.paintball = [LeaderboardData(arena) for arena in board["PAINTBALL"]]
        self.skywars = [LeaderboardData(arena) for arena in board["SKYWARS"]]
        self.murder_mystery = [
            LeaderboardData(arena) for arena in board["MURDER_MYSTERY"]
        ]
        self.super_smash = [LeaderboardData(arena) for arena in board["SUPER_SMASH"]]
        self.duels = [LeaderboardData(arena) for arena in board["DUELS"]]
        self.speed_uhc = [LeaderboardData(arena) for arena in board["SPEED_UHC"]]
        self.tnt_games = [LeaderboardData(arena) for arena in board["TNTGAMES"]]
        self.bedwars = [LeaderboardData(arena) for arena in board["BEDWARS"]]
        self.gingerbread = [LeaderboardData(arena) for arena in board["GINGERBREAD"]]
        self.build_battle = [LeaderboardData(arena) for arena in board["BUILD_BATTLE"]]
        self.arcade = [LeaderboardData(arena) for arena in board["ARCADE"]]
        self.skyclash = [LeaderboardData(arena) for arena in board["SKYCLASH"]]
        self.quakecraft = [LeaderboardData(arena) for arena in board["QUAKECRAFT"]]
        self.true_combat = [LeaderboardData(arena) for arena in board["TRUE_COMBAT"]]
        self.walls3 = [LeaderboardData(arena) for arena in board["WALLS3"]]
        self.vampirez = [LeaderboardData(arena) for arena in board["VAMPIREZ"]]
