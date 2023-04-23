# import numpy as np

# def snail(array):
#     m = []
#     array = np.array(array)
#     while len(array) > 0:
#         m += array[0].tolist()
#         array = np.rot90(array[1:])
#     return m

# or 

def snail(snail):
    result = []
    while snail:
        result += snail.pop(0)
        if snail and snail[0]:
            for i in snail:
                result.append(i.pop())
        if snail:
            result += snail.pop()[::-1]
        if snail and snail[0]:
            for i in reversed(snail):
                result.append(i.pop(0))
    return result