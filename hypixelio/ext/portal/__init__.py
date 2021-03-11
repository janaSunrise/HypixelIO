import asyncio
import threading
import typing as t


class Portal:
    def __init__(self, stop_event: t.Any) -> None:
        self.loop = asyncio.get_event_loop()
        self.stop_event = stop_event

    @staticmethod
    async def _call(fn: t.Callable, args: t.Any, kwargs: t.Any) -> t.Any:
        return await fn(*args, **kwargs)

    async def _stop(self) -> None:
        self.stop_event.set()

    def call(self, fn: t.Callable, *args, **kwargs) -> t.Any:
        return asyncio.run_coroutine_threadsafe(self._call(fn, args, kwargs), self.loop)

    def stop(self) -> None:
        return self.call(self._stop)


def create_portal() -> t.Any:
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
