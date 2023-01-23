#!/usr/bin/env python3
"""Module that contains a function that handles pagination parameters
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a given page and page size
    Args: page (int): page specified
          page_size (int): page size specified
    Returns: Tuple of the index_range
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
