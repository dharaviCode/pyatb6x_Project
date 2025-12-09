print("Outside class1")

class MobilePhone:
    modal = None

    def __init__(self):   #Default constructor name
        print("Default constructor")

    def dail(self):
        print("Dailing")

samsung = MobilePhone() #Constructor will be called automatically whenever we create an Object
samsung.dail()
print("Outside class2")
