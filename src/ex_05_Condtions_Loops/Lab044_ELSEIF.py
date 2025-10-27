# Find the positive number is even or odd

num = int(input("Enter a positive number \n").strip())

if num >= 0:
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

else:
    print("Provide a positive number, it's a negative number")



# You can write short one-liner conditions using ternary operator:
"""
if num >= 0:
    print("Even" if num % 2 == 0 else "Odd")
else:
    print("Provide a positive number, it's a negative number")
"""