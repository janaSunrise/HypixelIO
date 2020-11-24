from dataclasses import dataclass


@dataclass
class CacheBackend:
    sqlite: str = "sqlite"
    mongodb: str = "mongodb"
    redis: str = "redis"
    memory: str = "memory"
