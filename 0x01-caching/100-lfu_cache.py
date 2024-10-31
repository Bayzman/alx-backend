#!/usr/bin/env python3
"""
A class LFUCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    A class for LFU caching system
    """
    def __init__(self):
        super().__init__()
        self.cache_data = {}
        self.lfu_count = {}
        self.usage_order = []

    def put(self, key, item):
        """
        A function that assigns key to item and handles LFU eviction
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.lfu_count[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used key
                lfu_key = min(self.lfu_count, key=self.lfu_count.get)
                # If multiple keys have the same frequency, use the LRU policy
                lfu_keys = [
                    k for k, v in self.lfu_count.items()
                    if v == self.lfu_count[lfu_key]
                ]
                if len(lfu_keys) > 1:
                    lfu_key = min(
                        lfu_keys, key=lambda k: self.usage_order.index(k)
                    )
                del self.cache_data[lfu_key]
                del self.lfu_count[lfu_key]
                self.usage_order.remove(lfu_key)
                print("DISCARD: " + lfu_key)

            self.cache_data[key] = item
            self.lfu_count[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        """
        A function that returns the value of key from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        self.lfu_count[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
