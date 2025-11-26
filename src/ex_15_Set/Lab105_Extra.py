squares = {x ** 2 for x in range(5)}   # {0, 1, 4, 9, 16}
print(squares)

qube = {x ** 3 for x in range(5)}
print(qube)

# Frozen Set (Immutable Set)
# A frozenset cannot be changed after creation.
my_list = [1, 2, 3, 3]
frozen_set = frozenset(my_list)
print(frozen_set)
frozen_set.add(4)  #AttributeError: 'frozenset' object has no attribute 'add'
