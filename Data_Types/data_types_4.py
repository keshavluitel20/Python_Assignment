def char_mixing(a, b):
    a1 = b[:2] + a[2]
    b1 = a[0:2] + b[2]

    return a1 + ' ' + b1


print(char_mixing("abc", "xyz"))
