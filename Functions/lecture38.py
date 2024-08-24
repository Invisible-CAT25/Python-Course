# print()
# input()

# function declaration
# def greet():
#     print("Good Morning!")
#     print("Dhruv")

# greet()

# print()

# def sum(a,b):
#     c = a+b
#     # print(c)
#     return c

# # print(a+b)
# # a = 5
# a = sum(2,2)
# print(a)

# a = int(input("Enter a Number : "))
# b = int(input("Enter a Number : "))


# def printcounting(n):
#     for i in range(n):
#         print(i)

# printcounting(11)

# def printEven(n):
#     for i in range(n):
#         if i%2==0:
#             print(i)

# printEven(11)

def func(a,b):
    if a>b:
        # print(a+b)
        return a+b
    else:
        # print(b-a)
        return b-a

print(func(5,7))