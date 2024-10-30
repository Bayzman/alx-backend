#!/usr/bin/env python3
"""
A class LIFOCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    A class for LIFO caching system
    """
    def __init__(self):
        super().__init__()
        self.cache_data = {}
        self.order = []

    def put(self, key, item):
        """
        A function that is used to assing key to item
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        self.order.append(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            newest_key = self.order[-2]
            self.order.remove(newest_key)
            del self.cache_data[newest_key]
            print("DISCARD: " + newest_key)

    def get(self, key):
        """
        A method that gets the value of a particular key value
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
