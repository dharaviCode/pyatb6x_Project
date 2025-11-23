pb_global_b = 12  #Global variable

def my_function():
    pb_a = 10  #Local variable
    print(pb_a)
    print(pb_global_b)

# print(pb_a)
print(pb_global_b) # - 12
my_function() # 10 , 12