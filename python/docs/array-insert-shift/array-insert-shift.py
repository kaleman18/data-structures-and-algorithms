


# def insert_Shift_Array(given_list, num):
#     left_index = 0
#     right_index = len(given_list)-1
#     if len(given_list) % 2 == 0:
#         while left_index <= right_index:
#             if left_index == right_index:
#                 given_list.insert(left_index, num)
#                 break
            
#             left_index += 1
#             right_index -= 1
#     else:
#         this_loop = True
#         while this_loop:
#             if left_index > right_index:
#                 given_list.insert(left_index, num)
#                 break
#             left_index += 1
#             right_index -= 1
#     return given_list


case1 = [2,4,6,-8] #[2,4,5,6,-8]
num1 = 5

case2 = [42,8,15,23,42] #[42,8,15,16,23,42]
num2 = 16

def insert_shift_array(given_list, num):
  mid = 0
  arrayLen = len(given_list)
  if arrayLen % 2 == 0:
    mid = arrayLen / 2
  else: 
    mid = arrayLen / 2 + 1
  
  leftArr = []
  rightArr = []
  
  for i in range(arrayLen):
    if i < mid:
      leftArr += [given_list[i]]
    else:
      rightArr += [given_list[i]]
  
  return leftArr + [num] + rightArr

print(insert_shift_array(case1, num1))
print(insert_shift_array(case2, num2))