"""This module is dedicated to definition of the Caching class."""

from .backend import CacheBackend
from requests_cache import core


class Caching:
    """
    This is the Custom Caching model, for the Hypixel Requests to be made.

    Attributes:
        cache_name (str): The name of the Cache, Which will be stored
        backend (CacheBackend): The format of storage of the Cache
        expire_after (int): When will the cahe expire, In seconds
        old_data_on_error (bool): Whether to use old data, If an error occurs out of no where.
    """
    def __init__(
        self,
        cache_name: str = "cache",
        backend: CacheBackend = CacheBackend.memory,
        expire_after: int = None,
        old_data_on_error: bool = False
    ) -> None:
        self.cache_name = cache_name
        self.backend = backend
        self.expire_after = expire_after
        self.old_data_on_error = old_data_on_error

    def remove_expired_responses(self) -> None:
        core.remove_expired_responses()

    def get_cache(self) -> core.CachedSession:
        return core.get_cache()

    def clear_cache(self) -> None:
        core.clear()

    def uninstall_cache(self) -> None:
        core.uninstall_cache()

    def __str__(self) -> str:
        return self.backend

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} cache_name="{self.cache_name}" backend="{self.backend}">'
