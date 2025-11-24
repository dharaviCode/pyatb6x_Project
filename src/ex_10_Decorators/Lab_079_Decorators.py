def add_security(func):

    def wrapper():
        print("1.start scooty")
        print("2.Check for driving licence")
        func()
        print("3.stop the scooty")
        print("4.Check for fuel indicator")
    return wrapper()


@add_security
def drive_ola_scooty():
    print("drive ola")

@add_security
def drive_mahindra_scooty():
    print("drive mahindra")

@add_security
def drive_ola_tata_scooty():
    print("drive tata scooty")