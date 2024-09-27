class Abc:
    a = 1000

    @classmethod
    def clsmethod(cls):
        print(f"value of a is {cls.a}")

obj = Abc()

Abc.a = 50

obj.clsmethod()
Abc.clsmethod()