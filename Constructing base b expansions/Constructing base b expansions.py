def exp(x, y):
    z = x
    k = 0
    a = []
    while z != 0:
        a.append(z % y)
        z = z / y
        k += 1

    return a


print(exp(8, 6))
