
class Dog:
    #Attributes
    name = None
    breed = None
    height = None
    weight = None
    race = None

    def __init__(self, givenName, givenBreed): #Parameterized constructor
        print("Parameterized constructor")
        #Initializing the class attribute values
        self.name = givenName
        self.breed = givenBreed

    #Behaviour
    def bark(self):
        print("Barking")

    def sleepy(self):
        print("Who is sleep -> " + self.name, self.breed)

    def talk(self):
        pass

#Object creation
chow = Dog("chow", "mastiff") #The moment we create an object constructor method will be called
chow.sleepy()
chow.bark()
pom = Dog("pom", "toy")
pom.sleepy()
pom.bark()