# Functions can have keywords in arguments

#Declare/Define
def display_info(name, role):
    print(f"Hello, {name}, I am {role}.")

#Calling
#Normal way
display_info("Avinash", "Engineer")

#Better version
display_info(name="Avinash", role="Engineer")
display_info(role="Engineer", name="Avinash") # We can put keywords at any place while calling