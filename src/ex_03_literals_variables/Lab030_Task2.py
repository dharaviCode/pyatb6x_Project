# Task for Today
# Take a 2 input from the user
# Print the Quotient and Remainder
# 15 ->  num1
# 2 -> num2
# Q -> 7
# R -> 1

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

quotient = num1 // num2 # for quotient we use //
remainder = num1 % num2 # for reminder we use %

print(quotient)
print(remainder)