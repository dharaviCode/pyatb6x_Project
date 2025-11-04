# Function with default parameter

#Define/Declare
def greet_with_default_param(name = "QA"):    #Default value is assinged
    print("Hi", name)

#Call
greet_with_default_param("Avinash")
greet_with_default_param(name="QA")
greet_with_default_param()  # If we do not provide any parameter when calling function then
                            # default value will be taken