class A:
    def __init__(self,a):
        print("C1 called")

    def demo1(self,a):
        print(f"hello doston {a}")

class B(A):
    def __init__(self):
        super().__init__(5)
        print("C2 called")

    def demo(self):
        super().demo1("kya")
        print("good morning")

obj = B()
obj.demo()