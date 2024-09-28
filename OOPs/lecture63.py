# class Abc:
#     a = 10
#     b = 50

#     def __init__(self,c,d):
#         self.a = c
#         self.b = d

# obj = Abc(2,3)
# obj2 = Abc(5,10)
# print(obj.a)
# # print(obj.a)
# # obj.a = 1000
# # obj.b = 5000

class Student:
    name = ''
    roll_n0 = 0
    marks = 0

    def __init__(self,name,roll,marks):
        self.name = name
        self.roll_n0 = roll
        self.marks = marks

s1 = Student("rahul",10,90)
s2 = Student("vikas",20,80)

print(s1.name,s1.roll_n0)