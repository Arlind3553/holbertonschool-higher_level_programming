#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nList = []
    for i in range(list_length):
        try:
            result = my_list_1 / my_list_2
        except TypeError:
            print("wrong type")
            resut = 0
        except ZeroDivisionError:
            print("division by 0")
            resut = 0
        except IndexError:
            print("out of range")
            resut = 0
        finally:
            nList.append(result)
    return nList
