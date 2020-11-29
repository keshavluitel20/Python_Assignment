def non_duplicate_list(l):
    new_list = []
    for a in l:
        if a not in new_list:
            new_list.append(a)
    return new_list


print(non_duplicate_list([1, 2, 3, 3, 3, 3, 4, 5]))
