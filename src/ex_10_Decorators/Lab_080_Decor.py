def before_after_ui_test(func):

    def wrapper():
        print("Before running UI code")
        func()
        print("After running UI code")
    return wrapper()


@before_after_ui_test
def test_ui():
    print("Hi, I am testing UI test")