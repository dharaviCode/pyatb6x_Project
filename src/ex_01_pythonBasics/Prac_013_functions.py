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



