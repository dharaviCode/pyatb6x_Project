#list = [2,5,3,1,8,4]

#print(type(list))

#set = {1,2,2,3,3,4}
#print(set)

numbers = [1,2,3,4,5,2,4,1,3]
unique = []
seen = set()
for x in numbers:
    if x not in seen:
        seen.add(x) # it just returns none / used only for memory
print(seen)