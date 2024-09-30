class Abc:

    def add(self,a):
        print(a)
    
    prev = add

    def add(self,a,b):
        print(a+b)
    
    prev1 = add

    def add(self,a,b,c):
        print(a+b+c)

obj = Abc()
obj.prev1(2,3)
    
