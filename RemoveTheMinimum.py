# numbers = [1, 2, 3, 4, 5]
# numbers.remove(min(numbers))
# print(numbers)


def remove_smallest(numbers): 
    if len(numbers) < 1:
        return numbers
    else:
        numbers.remove(min(numbers))
        return numbers
