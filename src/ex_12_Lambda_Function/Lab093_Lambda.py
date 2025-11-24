#Normal function
def sum_three_numbers(a,b,c):
    return a+b+c

print(sum_three_numbers(2,3,4))

#Converting to lambda

sum_three_number_l_f = lambda a,b,c: a+b+c
print(sum_three_number_l_f(2,3,4))