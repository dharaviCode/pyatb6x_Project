# Function can return multiple values

#Define/Declare
def math_operation(a,b):
    return a+b, a-b, a*b, a/b

#Calling
sum_res, diff_res, mul_res, div_res = math_operation(4,5)
print(sum_res)
print(diff_res)
print(mul_res)
print(div_res)