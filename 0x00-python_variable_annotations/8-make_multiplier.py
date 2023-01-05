#!/usr/bin/env python3
"""Define a function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""

    def multiply(x: float) -> float:
        """return a multiplication of float"""
        return x * multiplier
    
    return multiply
