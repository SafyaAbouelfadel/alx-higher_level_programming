#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxv = 0
    maxk = None
    for key, value in a_dictionary.items():
        if value > maxv:
            maxv = value
            maxk = key
    return maxk
