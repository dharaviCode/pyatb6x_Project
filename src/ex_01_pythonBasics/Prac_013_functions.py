def greet():
    print("hi")

greet()
greet()
#################################
def greet_with_parameter(name): #defining the function
    print("hi", name)    #piece of code (logic)

greet_with_parameter("Avinash") #calling the funtion
greet_with_parameter("Dharani")
#################################
def returning_function(a, b):
    return a+b, a-b, a*b, a/b

sum_r, diff_r, mul_r, div_r = returning_function(10, 20)
print(sum_r, diff_r, mul_r, div_r)
##################################
def default_value_function(name = "QA"):
    print(f"Hello, {name}")

default_value_function("Avinash")
default_value_function()
##################################
def function_with_keywords(name, role, age):
    print(f"Hello {name} and your role is {role} with only age {age}")

function_with_keywords(age = 21, role = "Administrator", name = "Avinash")
##################################
def nested_function1():
    print("Nested function1")

    def nested_function2():
        print("Nested function2")

    nested_function2()

nested_function1()
##################################
def calculator(a, b):
    return a+b, a-b, a*b, a/b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(calculator(a, b))
##################################
#functions with infinite arguments

def infinite_arg_function(*args): #here *args means we can pass any number of arguments
    for i in args:
        print(i)

infinite_arg_function("Avinash","Kumar",123,12.45,"Habit",3,5,7,8,2.445656,5676)

# like print() function is a funtion win which we can pass unlimited number of arguments/parameters
###################################
#function scope
num_gb = 14 # global variable / outside the scope of function

def function1():
    print(num_gb)
    num_lc = 10 #local variable/inside the scope of a function
    print(num_lc)

print(num_gb) #global variable can be printed outside of function
# print(num_lc) # local variable which was defined inside a function cannot be printed outside of the scope
function1()
####################################
#inner function
def outer_function():
    var1 = 90
    print(var1)
    def inner_function1():
        var2 = 90
        print(var1)
    def inner_function2():
        var3 = 90
        print(var1)

    inner_function1()
    inner_function2()

    #print(var2, var3) #This is not possible as these are declared inside inner function
outer_function()



