"""This module is dedicated to definition of the Caching class."""

from requests_cache import core

from .backend import CacheBackend


class Caching:
    """
    This is the Custom Caching model, for the Hypixel Requests to be made.
    """
    def __init__(
        self,
        cache_name: str = "cache",
        backend: str = CacheBackend.memory,
        expire_after: int = None,
        old_data_on_error: bool = False
    ) -> None:
        """
        The Constructor for the Caching Model.

        Args:
            cache_name (str, optional): The name of the Cache, Which will be stored. Defaults to "cache".
            backend (str, optional): The format of storage of the Cache. Defaults to CacheBackend.memory.
            expire_after (int, optional): When will the cahe expire, In seconds. Defaults to None.
            old_data_on_error (bool, optional): Whether to use old data, If an error occurs.. Defaults to False.
        """
        self.cache_name = cache_name
        self.backend = backend
        self.expire_after = expire_after
        self.old_data_on_error = old_data_on_error

    def remove_expired_responses(self) -> None:
        """
        Remove the expired responses stored in the cache.
        """
        core.remove_expired_responses()

    def get_cache(self) -> core.CachedSession:
        """
        Get the cache, which is currently stored and being used.

        Returns:
            core.CachedSession: The cache stored and used currently.
        """
        return core.get_cache()

    def clear_cache(self) -> None:
        """
        Clear the cache stored in the storage specified.
        """
        core.clear()

    def uninstall_cache(self) -> None:
        """
        Remove caching from your code, if added or integrated.
        """
        core.uninstall_cache()

    def __str__(self) -> str:
        return self.backend

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} cache_name="{self.cache_name}" backend="{self.backend}">'
