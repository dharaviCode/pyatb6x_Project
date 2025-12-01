
dict1 = {"a": 1, "b": 2, "c": 3}

print(dict1.keys())
print(dict1.values())

dict2 = {"a": 1, "b": 2}

#missing_keys = dict1.values() - dict2.values() #TypeError: unsupported operand type(s) for -: 'dict_values' and 'dict_values'
missing_keys = set(dict1.keys() - dict2.keys())
print(missing_keys)

missing_values = set(dict1.values())-set(dict2.values())
print(missing_values)