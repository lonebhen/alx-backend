#!/usr/bin/env python3

"""Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):

    def put(self, key, item):
        """Put method"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get method"""
        if key in self.cache_data:
            return self.cache_data[key]
