class Car:
    #Instance variables
    name = None
    make = None
    modal = None

    #Constructor created for initializing the instance variables
    def __init__(self, name_car, make_car, modal_car):
        self.name = name_car
        self.make = make_car
        self.modal = modal_car

    def start_engine(self):
        print("Starting a car with the name " + self.name)
        print("Starting a car with make " + self.make)
        print("Starting a car with modal " + self.modal)


lambo = Car("lambo", "turbo", "2019")
lambo.start_engine()

thar = Car("thar", "4X4", "2022")
thar.start_engine()