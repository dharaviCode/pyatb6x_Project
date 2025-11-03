print("Enter which test you want to execute\n")

test_type = input("enter the test_type: API, UI, Performance, Security: ").strip()
#match-case
match test_type:
    case "API":
        print("Running postman API")
    case "UI":
        print("Running selenium UI")
    case "Performance":
        print("Running performance")
    case "Security":
        print("Running security")
    case _:
        print("Invalid test type")

# Above code can be written using if - elif as well

# test_type = input("Enter the test type: ").strip()
#
# if test_type == "API":
#     print("We are running a POSTMAN API Testcase.")
# elif test_type == "UI":
#     print("We are running a Selenium Testcase.")
# elif test_type == "Performance":
#     print("We are running a Performance Testcase.")
# elif test_type == "Security":
#     print("We are running a Security Testcase.")
# else:
#     print("Invalid Type.")