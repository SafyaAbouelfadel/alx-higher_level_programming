#!/usr/bin/python3
for i in range(10):
    for k in range(i, 10):
        if i < k:
            print("{}{}".format(i, k),
                end="\n" if i == 8 and k == 9 else ", ")
