# class A:
#     def demo(self):
#         print("hello doston")

# class B(A):
#     def demo(self,a):
#         print("hello world")

# obj = B()
# obj.demo(5)

class A:
    a = 10
    def demo(self):
        print("1")
class B:
    a = 30
    def demo1(self):
        print("2")
class C(A,B):
    a = 5
    # def demo(self):
    #     print("3")
    pass

obj = A()
print(obj.demo1)
print(A.__mro__)