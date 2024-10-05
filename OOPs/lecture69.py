class A:
    a = 10

class B(A):
    b = 20

class C(A):
    c = 30

obj = B()
obj2 = C()

print(obj.a)
print(obj.b)
print(obj2.c)
print(obj2.a)