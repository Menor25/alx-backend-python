#!/usr/bin/env python3
"""Define a coroutine called async_comprehension that takes no arguments"""
from typing import List

async_generator = __import__('0-async_generator.py').async_generator


async def async_comprehension() -> List[float]:
    """Return 10 random numbers"""
    return [i async for i in async_generator()]
