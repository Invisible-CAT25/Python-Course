class Student:
    name = "Rahul"
    class_name = 12
    roll_no = 3
    marks = 90
    subject = "Maths"

s1 = Student()
s2 = Student()
s2.name = "Ritik"
s2.class_name = 12
s2.roll_no = 67
s2.marks = 67
s2.subject = "physics"
print(s2.name)
print(s1.name)

print(Student.__dict__)

