nums = [1,2,3,4,5,6,7,8,9]

def even_num(x):
    return x % 2 == 0

print_even_numbers = list(filter(even_num, nums))  #Filter will find all the elements that return true
print(print_even_numbers)                          #filter(function, list)

list_student = [50, 51, 100]

def keep(x):
    if x > 50:
        return True

all_student = list(filter(keep,list_student))
print(all_student)
