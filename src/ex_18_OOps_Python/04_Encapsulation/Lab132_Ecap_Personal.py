class Home:

    def __init__(self):
        self.public_var = 'father'
        self._protected_var = 'brother'
        self.__private_var = 'baby'

    def mom(self):
        print(self.__private_var) #this method can access the private var
        self.__wife()
        print(self.public_var)

    def __wife(self):
        print("Private Wife")

object_ref = Home()
#object_ref.wife() - # Cannot directly call a private method
#object_ref.__private_var - # Cannot directly call a private variable

object_ref.mom()  #Public method mom can call all private method or var which is here called encapsulation.

print(object_ref._protected_var) # ⚠️ Technically accessible, but not recommended
