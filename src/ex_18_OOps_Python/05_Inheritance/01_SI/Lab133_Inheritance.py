# Single Inheritance
# A Subclass/Child/Son class inherits attributes and method from one Parent/Base/Father class

class BaseTest:
    driver = "Chrome"
    __driver2 = "FF"

    def setup(self):
        print("Base setup with the browser and env "+ self.__driver2)


class LoginTest(BaseTest):
    def run(self):
        self.setup()    # Here this method belongs to parent class and can be used by child class
        print("Running the test cases "+ self.driver) #Also the attributes of parent class can be used by child class
                                                        #The private variable or method of parent class cannot be used or accessed directly by the child class
t = LoginTest()
t.run()