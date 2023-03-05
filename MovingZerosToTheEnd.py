def move_zeros(lst):
#     x = len(lst)
#     j = 0
#     for i in range(x):
#         if lst[i] != 0:
#             return lst[j], lst[x] = lst[x], lst[j]
        
#         j = j + 1
#     return lst 

    nonZeroValues = [x for x in lst if x != 0]
    zeroes = [j for j in lst if j == 0]
    lst = nonZeroValues + zeroes
    return lst
