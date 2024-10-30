#!/usr/bin/env python3

""" FIFO Caching """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO Caching """
    def __init__(self):
        """ class constructor """
        super().__init__()

    def put(self, key, item):
        """ Adds item to the specified key """
        if (key or item) is None:
            pass

        self.cache_data[key] = item

        if (len(self.cache_data)) > BaseCaching.MAX_ITEMS:
            for key in self.cache_data.keys():
                self.cache_data.pop(key)
                print(f'DISCARD: {key}')
                break

    def get(self, key):
        """ gets the value of the specified key """
        if (key is None):
            return None

        return self.cache_data.get(key)
