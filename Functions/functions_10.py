def check_even_num(l):
    even_num = []
    for n in l:
        if n % 2 == 0:
            even_num.append(n)
    return even_num


print(check_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))
