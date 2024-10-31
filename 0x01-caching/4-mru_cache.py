#!/usr/bin/env python3
"""
A class MRUCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    A class for MRU caching system
    """
    def __init__(self):
        super().__init__()
        self.recent = []  # Keeps track of the usage order of keys

    def put(self, key, item):
        """
        A function that assigns key to item and handles MRU eviction
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.recent.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # If the cache is at maximum capacity, remove the MRU item
            mru_key = self.recent.pop(-1)  # Remove the most recently used key
            del self.cache_data[mru_key]  # Remove the MRU key from the cache
            print("DISCARD: " + mru_key)

        # Add the new key to the end of recent list and cache_data
        self.recent.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        A method that gets the value of a particular key
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the recent list to mark the key as most recently used
        self.recent.remove(key)
        self.recent.append(key)
        return self.cache_data[key]
