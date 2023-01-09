#!/usr/bin/env python3
"""Defines an async function called wait_n"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax.py").wait_random


async def wait_n(n: int, max_dely: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay
        return the list of all the delays (float values)
    """
    array = [wait_random(max_dely) for i in range(n)]
    return [await x for x in asyncio.as_completed(array)]
    