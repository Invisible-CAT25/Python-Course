class A:
    a = 10

    def p(self):
        print(self.a)

class B(A):
    b = 15
    c = 78

obj = A()
obj2 = B()
obj2.p()
print(obj2.b)
obj.p()
print(obj.b)