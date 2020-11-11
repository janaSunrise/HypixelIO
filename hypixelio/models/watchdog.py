"""This module is dedicated to definition of the Key class."""


class Watchdog:
    """
    This is the definition of the Custom Hypixel API Key Model.

    Attributes:
        data (dict): This contains the Returned JSON Response for the Watchdog API Request.
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

    def __str__(self) -> str:
        return self.LAST_MINUTE_BAN

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} last_minute_ban={self.LAST_MINUTE_BAN} rolling_daily={self.WATCHDOG_ROLLING_DAILY}>'

    def __hash__(self) -> int:
        return hash(self.LAST_MINUTE_BAN)
