#!/usr/bin/env python3
import time
import asyncio

async_comprehension = __import__('1-async_comprehension.py').async_comprehension


async def measure_runtime() -> float:
    """measure the total runtime and return it"""

    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    return time.perf_counter() - start