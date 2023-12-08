import asyncio
from .stops import Stops
from .routes import Routes
from .eta import ETA


def runner(func):
    def run():
        loop=asyncio.get_event_loop()
        return loop.run_until_complete(func())
    return run()