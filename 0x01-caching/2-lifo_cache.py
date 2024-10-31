#!/usr/bin/env python3

""" LIFO Caching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Caching """
    def __init__(self):
        """ class constructor """
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """ adds item to the specified key """
        if (key is None) or (item is None):
            return

        if key in self.cache_data:
            self.key_order.remove(key)
        self.cache_data[key] = item
        self.key_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.key_order[-2]
            self.cache_data.pop(last_key)
            print(f'DISCARD: {last_key}')
            del self.key_order[-2]

    def get(self, key):
        """ gets the value of the specified key """
        if (key is None):
            return None

        self.cache_data.get(key)
