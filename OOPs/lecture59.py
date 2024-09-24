class Abc:
    a = 10
    b = 20

obj1 = Abc()
obj2 = Abc()
# print(obj1)

# Abc.a = 500
# Abc.b = 600

# obj1.a = 500
# obj2.a = 700

# Abc.a = 1000
# obj1.a = 500

Abc.a = 1000
obj1.a = 500

print(Abc.a)
print(Abc.b)
print(obj1.a)
print(obj1.b)
print(obj2.a)
print(obj2.b)