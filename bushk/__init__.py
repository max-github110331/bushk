import asyncio
from .stops import Stops


def Task(func):
    def run():
        return asyncio.get_event_loop().run_until_complete(func())
    return run()