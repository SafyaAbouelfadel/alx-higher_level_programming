#!/usr/bin/python3
def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False

def uppercase(str):
    for a in str:
        print("{:a}".format(ord(a) if not is lower(a) else ord(a) - 32), end="")
        print("")
