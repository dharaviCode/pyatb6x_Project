# Function with parameters
#Define/Declare
def greet(name):
    print("Hello", name)

#Calling function
greet("Kumar")
greet("Avinash")
greet(24.56)
greet(-1)

#Define/declare
def greet_first_last_name(firstName, lastName):
    print("Hello", firstName, lastName)

#Calling the function
greet_first_last_name("Kumar", "Avinash")
greet_first_last_name(1234, 4321)

#Can function name be in uppercase - Yes can be but ideally we should use lowercase for
# function naming.
def FUNCTION_NAME(name):
    print("Hello", name)

FUNCTION_NAME("KUMAR")


