a = {1, 2, 3}
b = {3, 4, 5}
# print(a | b)    #Union of sets        # {1, 2, 3, 4, 5}
# print(a.union(b))       # same result
#
#
# print(a & b)            # {3} #Intersection of sets
# print(a.intersection(b)) # same result
#
# print(a-b)              # difference of sets
# print(b-a)              # difference of sets
#
print(a ^ b)            # SET SYMMETRIC DIFFERENCE

set1 = {1, 2, 3}
set2 = {4, 5, 6}
my_set = set1.union(set2)
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

my_set = set1.intersection(set2)
print(my_set)

my_set = set1.difference(set2)
print(my_set)

my_set = set2.difference(set1)
print(my_set)