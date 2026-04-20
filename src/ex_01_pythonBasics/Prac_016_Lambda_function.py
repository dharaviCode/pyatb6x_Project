# Normal function with only one expression can be converted into a single line using a function
# called a LAMBDA function

#Normal function:
def find_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

#Lambda function for the above normal function:

user_input = int(input("Enter your number: "))
check_even_odd_f = lambda num: "Even" if num % 2 == 0 else "Odd"
print(check_even_odd_f(user_input))

####################################################
# Normal function:
def triple_num(num):
    return num * 3

#Lambda function:
triple_func = lambda num: num * 3
print(triple_func(5))
