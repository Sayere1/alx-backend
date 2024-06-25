#!/usr/bin/env python3
"""FIFo caching"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """class FIFOCache that inherits from BaseCaching n is a caching system"""
    def __init__(self):
        """Cache initialized."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign an item to the self.cache_data."""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        return self.cache_data.get(key, None)
