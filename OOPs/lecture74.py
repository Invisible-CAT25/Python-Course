class A:
    a = 10
    _b = 20
    __c = 30

    def demo(self):
        print(self.a)
        print("hello")
    
    def _demo2(self):
        print("world")
    
    def getter(self):
        return self.__c

    def setter(self,c):
        self.__c = c
    
class B(A):
    def demo1(self):
        print(self._b)
        print(self._A__c)

obj = A()
# obj.demo()
# print(obj.a)
# print(obj._b)
# obj._demo2()
# # print(obj.__c)
# print(obj.getter())
# obj.setter(50)
# print(obj.getter())
# print(obj._A__c)
# print(A.__dict__)

obj = B()
obj.demo1()