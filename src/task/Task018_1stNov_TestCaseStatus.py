#Write a Function to Check Test Case Status
#Problem:
#Write a function check_status(status_code) that returns:
#"PASS" if status_code = 200
#"FAIL" if status_code = 400 or 500
#"UNKNOWN" otherwise
#Example Input & Output:
#print(check_status(200))   # PASS
#print(check_status(500))   # FAIL
#print(check_status(302))   # UNKNOWN
import sys


#define/declare
def check_status(status_code):
    match status_code:
        case 200:
            return "Pass"
        case 401:
            return "Fail"
        case 400:
            return "Fail"
        case 500:
            return "Fail"
        case _:
            return "Unknown error"

#Calling
status_code = int(input("enter the test case status: "))

result = check_status(status_code)
print(result)