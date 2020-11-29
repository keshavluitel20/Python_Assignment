def str_both_ends(str):
    if len(str) < 2:
        return ''
    else:
        return str[0:2] + str[-2:]


print(str_both_ends('Python'))
print(str_both_ends('Py'))
print(str_both_ends('w'))
