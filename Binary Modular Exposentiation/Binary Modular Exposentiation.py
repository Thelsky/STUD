def power(a, b, p):
    result = 1

    a = a % p

    if (a == 0):
        return 0

    while (b > 0):

        if ((b & 1) == 1):
            result = (result * a) % p

        b = b >> 1
        a = (a * a) % p

    return result


a = 25
b = 50
p = 6
print("The Power is : ", power(a, b, p))
