class Dog:
    #A
    name = None
    breed = None
    height = None
    weight = None

    #B
    def bark(self):
        print("Barking")
        # print(name)
        print(self.name)

    def talk(self):
        print("Talking")

print("Outside ?")
chow  = Dog() #Object_reference = Object()
chow.bark()   #calling method with the help of object_reference
# Dog() - Object
# chow -> Object Ref.

rancho = Dog()
rancho.bark()
#####################################################
class Car:
    name = None
    color = None
    brand = None

    def drive(self):
        print("Driving")
        print(self.name)
    def acc(self):
        print("Accelerating")
        print(self.brand)

mahindra = Car()
mahindra.drive()
mahindra.acc()



