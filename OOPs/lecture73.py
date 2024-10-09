from abc import ABC, abstractmethod

class A(ABC):
    
    @abstractmethod
    def printhello(self):
        pass

    @abstractmethod
    def printmorning(self):
        pass

    @abstractmethod
    def printnight(self):
        pass

class B(A):

    def printhello(self):
        print("Hello")

    def printmorning(self):
        print("Morning")

    def printnight(self):
        print("Night")

obj1 = A()
obj = B()
obj.printhello()