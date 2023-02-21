#!/usr/bin/env python3

"""
    Pagination
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    pagination parameters
    """

    index = (page*page_size) - page_size
    index_1 = index + page_size
    return (index, index_1)
