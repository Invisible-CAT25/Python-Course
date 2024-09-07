# def decorator(func):
#     def inner(a,b):
#         print("Compiler is doing the sum")
#         func(a,b)
#         print("Sum is done!")
#     return inner

# @decorator
# def add(a,b):
#     print(a+b)

# @decorator
# def sub(a,b):
#     print(a-b)

# # add(5,7)
# sub(9,7)

# def outer(func):
#     def inner(a,b):
#         return abs(func(a,b))
#     return inner

# @outer
# def sub(a,b):
#     return a-b

# print(sub(7,9))

# import time

# # print(time.time())
# print("hello")
# time.sleep(5)
# print("world")

import time

def timeofex(func):
    def inner(a,b):
        start = time.time()
        func(a,b)
        end = time.time()

        return end-start
    return inner

@timeofex
def mul(a,b):
    return (a*b)

print(mul(5,7))
