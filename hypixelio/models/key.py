"""This module is dedicated to definition of the Key class."""


class Key:
    """
    This is the definition of the Custom Hypixel API Key Model.
    """
    def __init__(
        self,
        key: str,
        owner_uuid: str,
        query_limit: int,
        queries_in_past_minute: int,
        total_queries: int,
    ) -> None:
        self.KEY = key
        self.OWNER_UUID = owner_uuid

        self.QUERY_LIMIT = query_limit
        self.QUERIES_IN_PAST_MINUTE = queries_in_past_minute
        self.TOTAL_QUERIES = total_queries
