#!/usr/bin/env python3

""" Returns a turn containing a start index and an end index corresponding """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ Returns a turn containing a start index and 
        an end index corresponding 
    """
    if (page == 1):
        start_idx, end_idx = (page - 1, page_size)
        return (start_idx, end_idx)

    elif (page > 1):
        start_idx = (page * page_size) - page_size
        end_idx = page * page_size
        return (start_idx, end_idx)

    else:
        return
