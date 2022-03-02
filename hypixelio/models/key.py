class Key:
    def __init__(self, data: dict) -> None:
        """
        Parameters
        ----------
        data: dict
            The JSON data received from the Hypixel API.
        """
        self.key = data["key"]
        self.owner_uuid = data["owner"]

        # Queries info
        self.query_limit = data["limit"]
        self.queries_in_past_minute = data["queriesInPastMin"]
        self.total_queries = data["totalQueries"]

    def __str__(self) -> str:
        return self.key

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} key="{self.key}" owner="{self.owner_uuid}">'

    def __hash__(self) -> int:
        return hash(self.key)

    def __eq__(self, other: "Key") -> bool:
        return self.key == other.key
