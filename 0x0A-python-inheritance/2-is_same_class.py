#!/usr/bin/python3
"""
This module contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """
    return true if obj is the exact class a_class, otherwise false

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj.

    Returns:
        True if obj is exactly an instance of a_class, False otherwise.
    """
    return (type(obj) == a_class)
