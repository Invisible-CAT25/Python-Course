class Grandpa:
    def land(self):
        print("Agriculture land")
    
class Father(Grandpa):
    def car(self):
        print("car")

class Child(Father):
    def loan(self):
        print("loan")
    
obj = Child()
obj.land()
obj.car()
obj.loan()