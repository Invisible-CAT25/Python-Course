class A:
    a = 10

class B:
    b = 20

class C(A,B):
    c = 30

obj = C()
print(obj.a)
print(obj.b)