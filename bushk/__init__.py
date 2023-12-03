import asyncio
from .stops import Stops
from .routes import Routes
from .eta import ETA


def Task(func):
    def run():
        return asyncio.run(func())
    return run()