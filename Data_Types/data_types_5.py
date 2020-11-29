def add_str(str):
    length = len(str)

    if length > 2:
        if str[-3:] == 'ing':
            str += 'ly'
        else:
            str += 'ing'

    return str


print(add_str('abc'))
print(add_str('string'))
