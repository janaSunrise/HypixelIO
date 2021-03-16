__all__ = (
    "Portal",
    "create_portal"
)

import asyncio
import threading
import typing as t


class Portal:
    def __init__(self, stop_event: t.Any) -> None:
        """
        The portal for async to sync conversion.

        Parameters
        ----------
        stop_event: t.Any
            The stop event.

        Examples
        --------
        .. codeblock:: python
            async def test(msg):
                await asyncio.sleep(0.5)
                print(msg)
                return "HELLO " + msg

            # It'll run a new event loop in separate thread
            portal = create_portal()

            # It'll call `test` in the separate thread and return a Future
            print(portal.call(test, "WORLD").result())

            # Stop the portal.
            portal.stop().result()
        """
        self.loop = asyncio.get_event_loop()
        self.stop_event = stop_event

    @staticmethod
    async def _call(fn: t.Callable, args: t.Any, kwargs: t.Any) -> t.Any:
        """
        Call the coroutine.

        Parameters
        ----------
        fn: t.Callable
            The function to be called.
        args: t.Any
            The function arguments.
        kwargs: t.Any
            The function kwargs.

        Returns
        -------
        t.Any
            The values returned by the function.
        """
        return await fn(*args, **kwargs)

    async def _stop(self) -> None:
        """
        Set the stop event.

        Returns
        -------
        None
        """
        self.stop_event.set()

    def call(self, fn: t.Callable, *args, **kwargs) -> t.Any:
        """
        Call the coroutine.

        Parameters
        ----------
        fn: t.Callable
            The function to be called.

        Returns
        -------
        t.Any
            The values returned by the function.
        """
        return asyncio.run_coroutine_threadsafe(self._call(fn, args, kwargs), self.loop)

    def stop(self) -> None:
        """
        Call the stop event.

        Returns
        -------
        None
        """
        return self.call(self._stop)


def create_portal() -> t.Any:
    """
    Create the portal object with function initialized.

    Returns
    -------
    t.Any
        The portal object.
    """
    portal = None

    async def wait_stop() -> None:
        nonlocal portal
        stop_event = asyncio.Event()
        portal = Portal(stop_event)
        running_event.set()
        await stop_event.wait()

    def run() -> t.Any:
        asyncio.run(wait_stop())

    running_event = threading.Event()
    thread = threading.Thread(target=run)
    thread.start()
    running_event.wait()

    return portal
