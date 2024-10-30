#!/usr/bin/env python3

""" Basic caching system """

# from base_caching import BaseCaching
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Basic caching system """
    def __init__(self):
        """ Constructor of the class """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """ adds items to the cache """
        if (key or item) is None:
            pass

        self.cache_data.update({key: item})

    def get(self, key):
        """ gets the value at the specified key """
        if (key is None) or (not key):
            return None

        return self.cache_data.get(key)
