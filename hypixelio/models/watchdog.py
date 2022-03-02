class Watchdog:
    def __init__(self, data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The JSON data received from the Hypixel API.
        """
        self.last_minute_ban = data["watchdog_lastMinute"]

        self.staff_rolling_daily = data["staff_rollingDaily"]
        self.rolling_daily = data["watchdog_rollingDaily"]

        self.staff_total_bans = data["staff_total"]
        self.total_bans = data["watchdog_total"]

    def __str__(self) -> str:
        return self.last_minute_ban

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} last_minute_ban={self.last_minute_ban} rolling_daily={self.rolling_daily}>"
