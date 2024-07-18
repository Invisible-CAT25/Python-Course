# print(dir(set))

a = {1,2,3,4}
b = {6,7,8,9}
c = {12,34,1,2}

# print(a.union(b,c))
# print(a)
# print(a.update(b))
# print(a)
# print(b)
# print(a.intersection(c))
# print(c.intersection_update(a))
# print(a.symmetric_difference(c))
# print(a.symmetric_difference_update(c))
# a.add("python")
# a.remove(5)
# a.discard(5)
# a.pop()
# a.pop()
# a.pop()
# a.pop()
# a.pop()
# print(c.difference(a))
# a.clear()
# print(a)
# print(c)

# print(a.isdisjoint(c))

d = {1,2,3,4,5,6}
e = {1,2,3,8}

# print(e.issubset(d))
f = {*d,*e}
print(f)