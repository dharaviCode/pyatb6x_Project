class TestExample:

    def __init__(self):
        self.driver = "Chrome"
        self._config = "STAG"
        self.__api__key = "ABCD12345"

    def show(self):
        print(f"Driver: {self.driver}")
        print(f"Config: {self._config}")
        print(f"APIKey: {self.__api__key}")

    def __private_method1(self):
        pass

    def __private_method2(self):
        pass

    def work(self):            #Here this method can access the private methods which is called encapsulation
        self.__private_method1()
        self.__private_method2()

obj = TestExample()

obj.show()
obj.work()

# Access levels:
# print(obj.driver)          # ✅ Public — accessible
# print(obj._config)         # ⚠️ Protected — accessible but discouraged
# print(obj.__api__key)     # ❌ Private — AttributeError
# no underscore - public
# _singleUnderScore - protected
# __doubleUnderScore - private