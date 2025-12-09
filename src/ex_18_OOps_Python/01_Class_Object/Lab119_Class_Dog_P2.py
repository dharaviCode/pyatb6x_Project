class Phone:
    number = None
    modal = None
    year = None

    def talk(self):
        print("talking")

    def dial(self):
        print("dialing")


samsung = Phone()
samsung.talk()
samsung.dial()

nokia = Phone()
nokia.talk()
nokia.dial()