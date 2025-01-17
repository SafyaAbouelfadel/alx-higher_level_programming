#!/usr/bin/python3
"""Definition of A peak Finder Algorithm."""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int or None: The peak element in the list or None if the list is empty.
    """
    n = len(list_of_integers)
    if not n:
        return None
    if n == 1:
        return list_of_integers[0]
    mid = n // 2
    if mid > 0 and list_of_integers[mid - 1] >= list_of_integers[mid]:
        return find_peak(list_of_integers[:mid])
    elif mid < n - 1 and list_of_integers[mid] <= list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    else:
        return list_of_integers[mid]
