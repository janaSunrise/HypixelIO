"""This module is dedicated to definition of the Key class."""


class Watchdog:
    """
    This is the definition of the Custom Hypixel API Key Model.
    """
    def __init__(
        self,
        data: dict
    ) -> None:
        self.LAST_MINUTE_BAN = data["watchdog_lastMinute"]

        self.STAFF_ROLLING_DAILY = data["staff_rollingDaily"]
        self.TOTAL_BANS = data["watchdog_total"]

        self.WATCHDOG_ROLLING_DAILY = data["watchdog_rollingDaily"]
        self.STAFF_TOTAL_BANS = data["staff_total"]
