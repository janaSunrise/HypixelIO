class Key:
    """This is the Custom Hypixel API Key Model."""
    def __init__(self, data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The JSON data received from the Hypixel API.
        """
        self.KEY = data["key"]
        self.OWNER_UUID = data["owner"]

        self.QUERY_LIMIT = data["limit"]
        self.QUERIES_IN_PAST_MINUTE = data["queriesInPastMin"]
        self.TOTAL_QUERIES = data["totalQueries"]

    def __str__(self) -> str:
        return self.KEY

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} key="{self.KEY}" owner="{self.OWNER_UUID}">'

    def __hash__(self) -> int:
        return hash(self.KEY)

    def __eq__(self, other: "Key") -> bool:
        return self.KEY == other.KEY

    def __gt__(self, other: "Key") -> bool:
        return self.TOTAL_QUERIES > other.TOTAL_QUERIES

    def __ge__(self, other: "Key") -> bool:
        return self.TOTAL_QUERIES >= other.TOTAL_QUERIES
