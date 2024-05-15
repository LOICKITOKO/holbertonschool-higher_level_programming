#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            try:
                dividend = float(my_list_1[i])
                divisor = float(my_list_2[i])
            except ValueError:
                print("wrong type")
                result_list.append(0)
                continue

            if divisor == 0:
                print("division by 0")
                result_list.append(0)
            else:
                result = dividend / divisor
                result_list.append(result)

        except IndexError:
            print("out of range")
            result_list.append(0)

    return result_list
