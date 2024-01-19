case1 = [4, 8, 15, 16, 23, 42]  #2
num1 = 15              
case2 = [-131, -82, 0, 27, 42, 68, 179]  #4
num2 = 42     
case3 = [11, 22, 33, 44, 55, 66, 77]  #-1
num3 = 90        
case4 = [1, 2, 3, 5, 6, 7]  #-1
num4 = 4                   


def binary_search(list, target):
    new_list = []

    while list:
        min = list[0]
        for x in list:
            if x < min:
                min = x 
        new_list.append(min)
        list.remove(min)

    def search(sorted_list, target, left_index, right_index):
        if left_index > right_index:
            return -1
        
        mid = (left_index + right_index) // 2

        potential_match = sorted_list[mid]

        if target == potential_match:
            return mid
        
        elif target < potential_match:
            return search(sorted_list, target, left_index, mid - 1)

        elif target > potential_match:
            return search(sorted_list, target, mid + 1, right_index)
        

    return search(new_list, target, 0, len(new_list)-1)

print(binary_search(case1, num1))
print(binary_search(case2, num2))
print(binary_search(case3, num3))
print(binary_search(case4, num4))

        

    

