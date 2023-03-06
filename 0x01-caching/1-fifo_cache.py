#!/usr/bin/env python3

"""
    First in First Out Caching
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Fifo Caching"""

    def __init__(self):
        """Init and overloading"""
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        """Put method"""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                items_descaded = self.key_indexes.pop(0)
                del self.cache_data[items_descaded]
                print("DISCARD:", items_descaded)

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        """Get method"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
