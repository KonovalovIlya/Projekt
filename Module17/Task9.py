nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
new_list = []
dd = [[[new_list.append(k) for k in j] for j in i] for i in nice_list]
print(new_list)
