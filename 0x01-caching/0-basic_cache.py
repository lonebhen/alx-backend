#!/usr/bin/env python3

""" BaseCaching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Defines a class for caching information in key-value pairs
    Methods:
        put(key, item) - store a key-value pair
        get(key) - retrieve the value associated with a key
    """

    def put(self, key, item):
        """Put method"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get method"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
