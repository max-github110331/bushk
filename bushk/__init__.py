import asyncio
from .stops import Stops
from .routes import Routes


def Task(func):
    def run():
        return asyncio.run(func())
    return run()