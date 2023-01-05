#!/usr/bin/env python3
"""Define a function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """eturns their sum as a float"""
    return sum(mxd_lst)
