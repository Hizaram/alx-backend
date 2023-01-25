#!/usr/bin/env python3
"""Module that contains the class BasicCache"""
from parent_class import BaseCaching


class BasicCache(BaseCaching):
    """Class BasicCache that represents an object that allows storing
    and retrieval of items from a dictionary
    """
    def put(self, key, item):
        """Method that adds an object to the dictionary using the key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Method that retrieves an item from cache using the key"""
        return self.cache_data.get(key, None)
