#!/usr/bin/env python3
"""Define coroutine called async_generator that takes no arguments"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """Return a random number between 0 and 10"""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
