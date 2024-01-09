


def insert_Shift_Array(given_list, num):
    left_index = 0
    right_index = len(given_list)-1
    if len(given_list) % 2 == 0:
        while left_index <= right_index:
            if left_index == right_index:
                given_list.insert(left_index, num)
                break
            
            left_index += 1
            right_index -= 1
    else:
        this_loop = True
        while this_loop:
            if left_index > right_index:
                given_list.insert(left_index, num)
                break
            left_index += 1
            right_index -= 1
    return given_list


the_list = [42,8,15,23,42]
insert_number = 16
print(insert_Shift_Array(the_list, insert_number))