# Comprehensions

# List Comprehensions
# a = [i for i in range(10)]
# print(a)

# odd = []
# for i in range(10):
#     if i%2==0:
#         print(i)
#     else:
#         odd.append(i)

# print(odd)


# b = [i for i in range(10) if i%2==0]
# print(b)

# odd = []
# c = [i if i%2==0 else odd.append(i) for i in range(10)]
# print(c)
# print(odd)












# Ques-1
# a = [2*i for i in range(1,11)]
# print(a)

# for i in range(1,11):
#     print(2*i)


# t = ("python","hello","good","evening","hey","morning")

# l = [i if len(i)%2==0 else i[::-1] for i in t]
# print(l)

# for i in t:
#     if len(i)%2==0:
#         print(i)
#     else:
#         print(i[::-1])

# l = [2,3,4,2,3,4,5,6,7,6,7]

# s = {i for i in l}
# print(s)

# l = [1,2,3,4,5,6,7,8,9,10]

# d = {i:i*i for i in l}
# print(d)

l = ["python","hunny","bunny","dhruv","rohit"]