"""This module is dedicated to definition of the Caching class."""

from requests_cache import core

from .backend import CacheBackend


class Caching:
    """The Caching model for the Hypixel requests to be made and cached to save the request calls.."""
    def __init__(
        self,
        cache_name: str = "cache",
        backend: str = CacheBackend.memory,
        expire_after: int = None,
        old_data_on_error: bool = False
    ) -> None:
        """
        Parameters
        ----------
        cache_name: str
            The name of the Cache, Which will be stored. Defaults to "cache".
        backend: str
            The format of storage of the Cache. Defaults to CacheBackend.memory.
        expire_after: int
            When will the cache expire, In seconds. Defaults to None.
        old_data_on_error: bool
            Whether to use old data, If an error occurs. Defaults to False.
        """
        self.cache_name = cache_name
        self.backend = backend
        self.expire_after = expire_after
        self.old_data_on_error = old_data_on_error

    @staticmethod
    def remove_expired_responses() -> None:
        """Remove the expired responses stored in the cache."""
        core.remove_expired_responses()

    @staticmethod
    def get_cache() -> core.CachedSession:
        """
        Get the cache, which is currently stored and being used.

        Returns:
            core.CachedSession: The cache stored and used currently.
        """
        return core.get_cache()

    @staticmethod
    def clear_cache() -> None:
        """Clear the cache stored in the storage specified."""
        core.clear()

    @staticmethod
    def uninstall_cache() -> None:
        """Remove caching from your code, if added or integrated."""
        core.uninstall_cache()

    def __str__(self) -> str:
        return self.backend

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} cache_name="{self.cache_name}" backend="{self.backend}">'
