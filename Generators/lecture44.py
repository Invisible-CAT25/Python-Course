# def gen(a,b):
#     yield a+b
#     yield a-b
#     yield a*b
#     yield a**b

# # print(list(gen(5,10)))
# a = gen(5,10)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# a = [1,2,3,4,5,6,7,8,9]

# def sq(a):
#     for i in a:
#         yield (i**2)

# print(list(sq(a)))

# b = ["samsung","redmi","apple","vivo","oppo"]

# def ev(b):
#     for i in b:
#         if len(i)%2==0:
#             yield i

# print(list(ev(b)))

# c = [10,20,67,45,12,34,67,89]

# def odd(c):
#     for i in c:
#         if i%2 != 0:
#             yield i

# print(list(odd(c)))

# d = [12,45,67.8,"hello",[1,2,3],(2,3,4,6),34,"python"]

# def func(d):
#     for i in d:
#         if isinstance(i,(int,float,complex,bool)):
#             yield i

# print(list(func(d)))