"""This module is dedicated to definition of the Leaderboard data class."""


class LeaderboardData:
    """This is the Custom Hypixel API Leaderboard Data Model."""
    def __init__(self, data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The Leaderboard JSON data per game response received from the Hypixel API.
        """
        self.PATH = data['path']
        self.PREFIX = data['prefix']

        self.TITLE = data['title']

        self.LOCATION = data['location']
        self.COUNT = data['count']

        self.LEADERS_UUID = data['leaders']

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} title="{self.TITLE}" location="{self.LOCATION}">'

    def __str__(self) -> str:
        return self.TITLE
