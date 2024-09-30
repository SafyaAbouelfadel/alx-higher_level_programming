#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []

    for i in range (list_length):
        try:
            res_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            res_list.append(0)
            print("division by zero")
            continue
        except TypeError:
           res_list.append(0)
           print("wrong type")
           continue
        except IndexError:
            res_list.append(0)
            print("out of range")
            continue
        finally:
            pass

    return res_list
