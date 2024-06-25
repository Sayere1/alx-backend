#!/usr/bin/env python3
"""basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class BasicCache dat inherits from BaseCaching n is a caching system"""
    def put(self, key, item):
        """Assign an item to the self.cache_data."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """return none if the key doesn’t exist in self.cache_data"""
        return self.cache_data.get(key, None)
