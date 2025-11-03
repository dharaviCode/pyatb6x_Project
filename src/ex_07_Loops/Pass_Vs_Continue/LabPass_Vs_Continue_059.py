"""
for i in range(5):
    if i == 3:
        pass #Do nothing
    else:
        print("Number is : ", i)
        """

for i in range(5):
    if i == 3:
        continue #Skip the current iteration and move to next iteration of the loop
    else:
        print("Number is : ", i)