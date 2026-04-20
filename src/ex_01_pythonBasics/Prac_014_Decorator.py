# Decorator in python is nothing but a way to modify the behavior of the existing function or class
# without changing its source code.
# or we define it as decorator enhances the behaviour of the function without changing its actual behavior
# it is basically used for logging mechanism and before or after action in test case


def before_after_ui_function(func):
    def wrapper():
        print("Before, open chrome using webdriver")
        func()
        print("After, close chrome using webdriver")
    return wrapper()

def before_after_api_function(func):
    def wrapper():
        print("Before, open api using request")
        func()
        print("After, close api using request")
    return wrapper()


@before_after_ui_function
def normal_test_ui_function():
    print("Testing the UI flow of the app")

@before_after_api_function
def normal_test_api_function():
    print("Testing the API flow of the app")

