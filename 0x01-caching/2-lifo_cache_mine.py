#!/usr/bin/env python3

""" LIFO Caching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Caching """
    def __init__(self):
        """ class constructor """
        super().__init__()

    def put(self, key, item):
        """ adds item to the specified key """
        if (key or item) is None:
            pass

        self.cache_data[key] = item
        key_list = list(self.cache_data.keys())

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print(f'DISCARD: {key_list[-2]}')
            self.cache_data.pop(key_list[-2])

        # elif key in (key_list):
        # and len(self.cache_data) <= BaseCaching.MAX_ITEMS:
        # self.cache_data[key] = item
        # print(f'DISCARD: {key}')

    def get(self, key):
        """ gets the value of the specified key """
        if (key is None):
            return None

        self.cache_data.get(key)
