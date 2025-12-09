class Calculator:

    #Attributes
    a = None
    b = None

    #Parameterized constructor
    def __init__(self, num1, num2):
        self.a = num1 #Initializing the attribute values
        self.b = num2

    def sum(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
    def mod(self):
        return self.a % self.b
    def pow(self):
        return self.a ** self.b

obj_ref = Calculator(int(input("Enter 1st num")), int(input("Enter 2nd num")))
print("sum is ",obj_ref.sum())
print("sub is ",obj_ref.sub())
print("mul is ",obj_ref.mul())
print("div is ",obj_ref.div())
print("mod is ",obj_ref.mod())
print("pow is ",obj_ref.pow())
