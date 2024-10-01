# print(4+5)
# print("hi"+"hello")
# print([1,2,3]+[4,5,6])

class Abc:
    a = 0
    b = 0

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self,other):
        return self.a + other.a, self.b+other.b

    # def __mul__(self,other):
    #     return self.a * other.a

obj1 = Abc(5,25)
obj2 = Abc(10,50)

# print(obj1+obj2)
# print(Abc.__add__(obj1,obj2))
print(obj1*obj2)