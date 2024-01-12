case1 = [ [1, 2, 3], [3, 5, 7], [1, 7, 10] ] #[6, 15, 18]

case2 = [ [0, 1, 5], [-4, 7, 2], [-3, 12, 11] ] #[6, 5, 20]

def sum_matrix(matrix):
    new_list = []
    for sublist in matrix:
        list_sum = 0
        for j in range(len(sublist)):
            list_sum += sublist[j] + sublist[]
    new_list.append(list_sum)
    print(new_list)

sum_matrix(case1)