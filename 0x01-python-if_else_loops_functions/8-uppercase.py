#!/usr/bin/python3
def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False


def uppercase(str):
    for a in str:
        print("{:c}".format(ord(a) if not islower(a) else ord(a) - 32), end="")
    print("")
