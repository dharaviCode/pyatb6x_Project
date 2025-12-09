a = 10 # variable everywhere in the program
class Person:
    b = 11 # Instance variable - Variable inside a class but outside of method

    def print_info(self):
        c = 20 #     Local variable - Inside a method
        print(c)
        print(self.b)
        print(a)


object_ref = Person()
object_ref.print_info()

#below two are not possible in python as they are allocated inside a class and method
#print(b)
#print(c)