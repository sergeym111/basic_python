source_list = [12, 58, 14, 11, 55, 69, 1, -3]
print(source_list)
new_list = [source_list[i] for i in range(1, len(source_list)) if source_list[i] > source_list[i - 1]]
print(new_list)
