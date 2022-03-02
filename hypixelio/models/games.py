class GameCount:
    def __init__(self, game: dict) -> None:
        """
        Parameters
        ----------
        game: dict
            The Game JSON data response received from the Hypixel API.
        """
        self.players = game["players"]
        self.modes = game.get("modes")

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} players="{self.players}" modes={self.modes}>'


class Games:
    def __init__(self, games: dict, player_count: int) -> None:
        """
        Parameters
        ----------
        games: dict
            The Games JSON list data response received from the Hypixel API.
        player_count: int
            The player count in the whole Hypixel Server.
        """
        self.player_count = player_count

        self.main_lobby = GameCount(games["MAIN_LOBBY"])
        self.tournament_lobby = GameCount(games["TOURNAMENT_LOBBY"])

        self.uhc = GameCount(games["UHC"])
        self.super_smash = GameCount(games["SUPER_SMASH"])
        self.legacy = GameCount(games["LEGACY"])
        self.build_battle = GameCount(games["BUILD_BATTLE"])
        self.battleground = GameCount(games["BATTLEGROUND"])
        self.walls3 = GameCount(games["WALLS3"])
        self.housing = GameCount(games["HOUSING"])
        self.speed_uhc = GameCount(games["SPEED_UHC"])
        self.duels = GameCount(games["DUELS"])
        self.replay = GameCount(games["REPLAY"])
        self.survival_games = GameCount(games["SURVIVAL_GAMES"])
        self.prototype = GameCount(games["PROTOTYPE"])
        self.murder_mystery = GameCount(games["MURDER_MYSTERY"])
        self.mcgo = GameCount(games["MCGO"])
        self.bedwars = GameCount(games["BEDWARS"])
        self.skyblock = GameCount(games["SKYBLOCK"])
        self.arcade = GameCount(games["ARCADE"])
        self.pit = GameCount(games["PIT"])
        self.tnt_games = GameCount(games["TNTGAMES"])
        self.skywars = GameCount(games["SKYWARS"])
        self.limbo = GameCount(games["LIMBO"])

        self.idle = GameCount(games["IDLE"])
        self.queue = GameCount(games["QUEUE"])

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__} lobby={self.main_lobby} idle={self.idle} queue={self.queue} "
            f"players={self.player_count}>"
        )
