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

        key_list = list(self.cache_data.keys())
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(key_list[-1])
            print(f'DISCARD: {key_list[-1]}')
            key_list.append(key)

    def get(self, key):
        """ gets the value of the specified key """
        if (key is None):
            return None

        self.cache_data.get(key)
