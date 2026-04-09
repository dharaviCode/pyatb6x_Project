age = 21
#print("Age of boy is" + age) - not possible as it will throw TypeError
print("Age of boy is " + str(age))

#By using the modern python (f-string)
age = 25
print(f"Age of girl is {age}")
print(f"Age of dog is {age}")
print(f"Age of machine is {age}")
print(f"Age of building is {age}")
print(f"Age of monument is {age}")
print(f"Age is just a number {age}")

age = 26
name = "Avinash"

print(f"Username is {name} and its age is {age}")

#List concatenation:
list1 = [1, 2, 3]
list2 = [3, 4, 5]
result1 = list1 + list2
print(result1)

### Concatenation not possible in set - TypeError
#set1 = {1, 2, 3}
#set2 = {3, 4, 5}
#result2 = set1 + set2
#print(result2)
###

tuple1 = (1, 2, 3)
tuple2 = (3, 4, 5)
result3 = tuple1 + tuple2
print(result3)

print("QA " * 3)