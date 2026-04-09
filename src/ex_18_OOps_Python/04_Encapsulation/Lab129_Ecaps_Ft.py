# Web automation - selenium
# Page - you are going to automate

class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "avinash.kumar@gmail.com" and self.password == "13244":
            print("Login, allowed")
        else:
            print("Login failed")

# email - #read from test data - Excel, CSV, env file
# password - #read from test data - Excel, CSV, env file

#creating an object reference which will call the constructor first that will initialize the class attributes/dataMember

avinash = VWOLoginPage("avinash.kumar@gmail.com", "13244")
avinash.login_confirm()