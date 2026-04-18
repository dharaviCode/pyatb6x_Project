"""
name = input("enter the string")
print(len(name))
print(type(name))

list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print(list3)
print(type(list3))
print(len(list3))
"""

input = input("enter a string")

temp = list(input)
print(temp) #['a', 'v', 'i', 'n', 'a', 's', 'h']
temp.reverse()
reverse_temp = ''.join(temp)
print(reverse_temp)


reverse_output = ''.join((reversed(input)))
print(reverse_output)
print(type(reverse_output))