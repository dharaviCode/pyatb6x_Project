public_toilet = "PB"  #Global variable

def home():
    private_toilet = "PT" #Local variable
    print(private_toilet)
    public_toilet = "LPB" #The global variable here is changed to local and priority will
                          # be give to the changed local variable first
    print(public_toilet)

home()