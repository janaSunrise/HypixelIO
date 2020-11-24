from dataclasses import dataclass


@dataclass
class CacheBackend:
    """
    The Backend Adapters avilable for the caching.
    """
    sqlite: str = "sqlite"
    mongodb: str = "mongodb"
    redis: str = "redis"
    memory: str = "memory"
