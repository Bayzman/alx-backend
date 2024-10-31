#!/usr/bin/env python3

""" Basic caching system """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic caching system """
    def __init__(self):
        """ Constructor of the class """
        BaseCaching.__init__(self)  # super().__init__() (alternatively)
        self.cache_data = {}

    def put(self, key, item):
        """ adds items to the cache """
        if (key is None) or (item is None):
            return

        self.cache_data[key] = item
        # self.cache_data.update({key: item})

    def get(self, key):
        """ gets the value at the specified key """
        if (key is None):
            return None

        return self.cache_data.get(key)
