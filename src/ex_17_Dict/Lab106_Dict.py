my_dict = {
    "name": "Avinash",
    "age": 0,
    "role": "QA",
    "exp": 3
}

print(my_dict)
print(my_dict["name"])
print(my_dict["age"])
print(my_dict["role"])
print(my_dict["exp"])

my_dict["role"] = "SDET"
print(my_dict)

del my_dict["exp"]
print(my_dict)

for key, value in my_dict.items():
    print(key, value)

print("age" in my_dict )
print("exp" in my_dict )