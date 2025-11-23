def outer_function():
    var1 = 30 # local variable which is global for below two inner functions

    def inner_function():
        var2 = 90
        print(var1)

    def inner_function2():
        print(var1)


    inner_function()
    inner_function2()

outer_function()
#inner_function() - This cannot be called outside.