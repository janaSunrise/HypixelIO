"""This module is dedicated to definition of the Key class."""


class Watchdog:
    """
    This is the definition of the Custom Hypixel API Key Model.
    """
    def __init__(
        self,
        last_minute_ban: int,
        staff_rolling_daily: int,
        total_bans: int,
        watchdog_rolling_daily: int,
        staff_total_bans: int
    ) -> None:
        self.LAST_MINUTE_BAN = last_minute_ban

        self.STAFF_ROLLING_DAILY = staff_rolling_daily
        self.TOTAL_BANS = total_bans

        self.WATCHDOG_ROLLING_DAILY = watchdog_rolling_daily
        self.STAFF_TOTAL_BANS = staff_total_bans
