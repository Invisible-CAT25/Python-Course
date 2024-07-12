# a = [89,78,45,12,34]

# Normla copy
# b = a

# print(id(a))
# print(id(b))

# a[1] = 0
# print(a)
# print(b)

# b = a.copy()

# print(id(a))
# print(id(b))

# a[1] = 0
# print(a)
# print(b)

from copy import deepcopy

c = [23,45,78,90,1,[23,56]]

d = deepcopy(c)
# d = c.copy()

# c[5][0] = 0
# d[5][0] = 0

print(id(c[5]))
print(id(d[5]))