from dataclasses import dataclass


@dataclass
class CacheBackend:
    """The Backend Adapters available for the caching."""
    sqlite: str = "sqlite"
    mongodb: str = "mongodb"
    redis: str = "redis"
    memory: str = "memory"
