name = ["Avinash", "Kumar", "Singh", "qa", "Avinash"]

def upper_case(string):
    return string.upper()

all_upper_case = set(map(upper_case, name)) # Set removes the duplicate values
print(all_upper_case)