source_list = [4, 5, 7, 6, 1, 2, 7, 5, 4, 9, 4, 5]
solved_list = [i for i in source_list if source_list.count(i) == 1]
print(solved_list)