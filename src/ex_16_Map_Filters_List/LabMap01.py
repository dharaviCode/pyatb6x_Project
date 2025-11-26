numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sq(x):
    return x ** 2

sq_all_numbers = list(map(sq, numbers))    # map(function, list) - function that need to be applied on al elements of the list
print(sq_all_numbers)