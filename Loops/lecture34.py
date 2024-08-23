a = [1,2,3,4,5]
b = "python is a programming language"

# i = 0
# while i<len(a):
#     print(a[i])
#     i = i+1

# for i in b:
#     print(i*2)

# for i in range(21,10,-1):
#     print(i)

# for i in reversed(b):
#     print(i)

# for i in enumerate(b):
#     print(i)

x = [1,2,3,4,5]
y = [5,6,7,8]
z = [9,10,11,12]

# for i in zip(x,y,z):
#     print(i)

from itertools import zip_longest

for i in zip_longest(x,y,fillvalue=25):
    print(i)