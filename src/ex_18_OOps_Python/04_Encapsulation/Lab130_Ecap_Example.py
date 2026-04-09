# Encapsulation
# Hide the data members (class variables, instance variables)
# by using only the methods

class Cars:
    def __init__(self):
        self.public_avinash = "avinash"
        #self.__private_avinash = "pass123"

    def nany(self):
        self.__private_avinash = "pass123"

object_ref = Cars()
print(object_ref.public_avinash)
# print(object_ref.__private_avinash) - this one will not be called as it's a private data member
# so to call the above private data member we need to have a method inside the class that can use the
# private data member and that method when called will print the private data member.

print(object_ref.nany())
