import asyncio
from .stops import Stops


def Task(func):
    def run():
        return asyncio.run(func())
    return run()