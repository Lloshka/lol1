list1 = [5, 2, 8, 1, 9]

list2 = [2, 4, 1, 3, 0]

sorted_list = [x for _, x in sorted(zip(list2, list1))]

print(sorted_list)