#Create a Person class where we will have five attributes and five behaviors.
# Make sure that each type of function is used,
# and I want you to also create the print function,
# which will print all the instance variable values.

class Person:
    #Attributes
    name = None
    age = None
    height = None
    weight = None
    phone = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Behaviour
    def talk(self):
        print( self.name," talking")

    def swim(self):
        print(self.name, " swimming")

    def walk(self):
        print(self.name," walking")

    def run(self):
        print(self.name," running")

    def read(self):
        print(self.name," reading")

    def print_info(self):
        print(self.name,"is",self.age,"years old")

amit = Person("amit", 30)

amit.talk()
amit.swim()
amit.walk()
amit.run()
amit.read()
amit.print_info()