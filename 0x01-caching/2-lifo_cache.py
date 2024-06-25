#!/usr/bin/env python3
"""LIFO Cache"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """class LIFOCache that inherits from BaseCaching n is a caching system"""
    def __init__(self):
        """cache initializes"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign an item to the self.cache_data."""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """return the value in self.cache_data linked to key or none"""
        return self.cache_data.get(key, None)
