from dataclasses import dataclass


@dataclass
class CacheBackend:
    """The Backend adapters available for the caching."""
    sqlite: str = "sqlite"
    redis: str = "redis"
    mongodb: str = "mongodb"
    memory: str = "memory"
