class A:
    a = 10

class B(A):
    b = 10

class C(A):
    c = 30

class D(B,C):
    d = 40

obj = D()
print(obj.a)
