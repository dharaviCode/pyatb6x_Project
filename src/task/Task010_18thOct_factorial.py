#Given a Number, you need to calculate the factorial of that number:
#n = 5 -> Taking the number as i/p
#Fact = 5×4×3*2*1 = 120
#Fact = 0 → 1,

num = int(input("Enter a number whose fact you want: "))
fact = 1    #It's a mandatory condition to be taken for factorial logic

if num < 0:  #Edge case
    print("Sorry, factorial cannot be less than zero")
elif num == 0: #Edge case
     print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):  #main logic
        fact = fact * i
    print("Factorial of:", num, "is", fact)


"""
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
"""
