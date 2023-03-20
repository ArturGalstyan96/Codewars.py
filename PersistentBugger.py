def persistence(n):
    # your code
    x = 0
    y = 1
    b = 1
    a = 1
    while n > 9:
        b = str (n)
        for j in range(len(b)):
            a *= int(b[j])
        x += 1
        n = a
        a = 1
    return x