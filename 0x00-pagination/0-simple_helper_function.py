#!/usr/bin/env python3
"""func named index_range that takes 2 integer arguments page n page_size."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size 2 containing a start index and an end index"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
