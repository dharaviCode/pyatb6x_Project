#1. create a (.env) file into the project
#2. now put all creds and info into it which will be used to access the website or login page
#3. To use that (.env) file we have to import load_dotenv function from dotenv library
#4. To extract/fetch details from (.env) file we have to import OS library
#5. dotenv library - created by python community
#6. OS (operating system) library - created by python guys

from dotenv import load_dotenv
import os
class VWOLoginPage:

    def __init__(self, email_arg, password_arg):

        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        load_dotenv()
        print(os.getenv("VWO_USERNAME"))
        print(os.getenv("VWO_PASSWORD"))
        if self.email == os.getenv("VWO_USERNAME") and self.password == os.getenv("VWO_PASSWORD"):
            print("Allowed, Login Sucess")
        else:
            print("Login Failed")


email = input("Enter the vwo login email ")
password = input("Enter the vwo login password ")

vwo_object_ref = VWOLoginPage(email,password)
vwo_object_ref.login_confirm()

print(os.name)