#!/usr/bin/env python3
"""Module that contains the class FIFOCache that operates on the
First-In First-Out principle"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """Class that allows the insertion and retrieval of items in a cache
    using the FIFO principle if limit is reached
    """
    def __init__(self):
        """The __init__ module"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
