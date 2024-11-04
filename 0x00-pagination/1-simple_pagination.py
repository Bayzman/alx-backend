#!/usr/bin/env python3

""" Returns a turn containing a start index and an end index corresponding """
import csv
import math
from typing import Tuple, List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ returns the appropriate page of the dataset """
        assert isinstance (page, int) and page > 0
        assert isinstance (page_size, int) and page_size > 0

        start_idx, end_idx = index_range(page, page_size)

        if start_idx >= len(self.dataset()):
            return []

        return self.dataset()[start_idx : end_idx]
