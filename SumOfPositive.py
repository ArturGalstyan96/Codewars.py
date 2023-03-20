def positive_sum(arr):
    x = 0
    for i in arr:
        if i > 0:
            x += i
    return x