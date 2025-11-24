# Write a program to calcuclate even and odd
# def find_even_odd(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

user_input = int(input("Enter a number: "))

check_even_odd_lambda_f = lambda num: "even" if num % 2 == 0 else "odd"
result = check_even_odd_lambda_f(user_input)
print(result)