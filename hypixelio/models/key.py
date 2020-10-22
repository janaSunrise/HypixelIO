"""This module is dedicated to definition of the Key class."""


class Key:
    """
    This is the Custom Hypixel API Key Model.

    Attributes:
        data (dict): This contains the Returned JSON Response for the Key Info API Request.
    """
    def __init__(
        self,
        data: dict
    ) -> None:
        self.KEY = data["key"]
        self.OWNER_UUID = data["owner"]

        self.QUERY_LIMIT = data["limit"]
        self.QUERIES_IN_PAST_MINUTE = data["queriesInPastMin"]
        self.TOTAL_QUERIES = data["totalQueries"]

    def __str__(self) -> str:
        return self.KEY

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} key="{self.KEY}" owner="{self.OWNER_UUID}">'
