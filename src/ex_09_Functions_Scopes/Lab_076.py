public_toilet = "PB"  #Global variable

def home():
    private_toilet = "PT"  #Local Variable
    print(public_toilet)
    print(private_toilet)

def stranger():
    print(public_toilet)
    #print(private_toilet) #-  this is private and cannot be called in another function

home()
stranger()