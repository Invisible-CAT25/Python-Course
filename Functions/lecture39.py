#Arguments
# def sum(a,b,c):
#     print(a+b)

# num1 = 2
# num2 = 3
# sum(num1,num2)

# sum(a=2,b=3)
# sum(2,b=3,5) -- error

# def minus(a,b,/):
#     return b-a

# print(minus(5,b=3))

# def minus(*,a,b):
#     return b-a

# print(minus(a=5,b=3))

# def sum(a,b,c,/,*,d,e):
#     return a+b+c+d+e

# print(sum(2,3,c=4,d=3,e=7))

# def sum(*args):
#     print(args)

# sum(1,2,3,4,5)

# def sum(**kwargs):
#     print(kwargs)

# sum(a=2,b=5,c=6)

# def sum(a,b,c=10):
#     print(a+b)

# sum(2,1)

# def ispalindrome(s):
#     if s==s[::-1]:
#         print("Ispalindrome")
#     else:
#         print("Not a palindrome")

# ispalindrome("mom")

def func(a):
    if isinstance(a,(list,str,tuple)):
        print(a[::-1])
    else:
        print(type(a))

func(2)