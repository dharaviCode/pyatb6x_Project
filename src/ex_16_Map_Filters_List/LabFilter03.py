names = ["QA", "", "Automation", "", "Tester"]

def non_empty(x):
    if x != "":
        return True

non_empty_names = list(filter(lambda x: x != "", names))
print(non_empty_names)

non_empty_names = list(filter(non_empty, names))
print(non_empty_names)