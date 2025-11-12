#Create a function which will take a positive number from the user and perform square of the number?
#i/o = 3
#o/p = 9

#declare/definition
def sq_of_num(num):
    return num ** 2

#Calling function
result = sq_of_num(int(input("enter the number: ")))
print("Square of number is:", result)