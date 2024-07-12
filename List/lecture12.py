print(dir(list))

# l = ["red",45,89,"blue",True]
# print(l[0])
# l[0] = "black"
# print(l)

# l.append(67)
# l.append("string")
# l.append([2,3,45])

# l.extend("string")
# l.extend([25,56,78])

# l.insert(0,"voilet")
# l.insert(3,"voilet")
# l.insert(3,4)

# l.pop()
# l.pop(0)

# l = ["red",45,89,"blue",True,[45,67,89],45,54,45,45,67,789,45]

# l.remove(89)
# l.remove()
# l.pop(5)

# l.clear()
# del l
# l[3].remove('u')

# print(l.count(45))
# print(l)

# print(l.index(12))
# l.reverse()
# print(l)

# l = [90,1,45,2,67,3,89,45,67,23,34,45]
l = ["hello","bye","a","good","morning","good night"]
# a to z ASCII VALUE -- 97 to 122
# A to Z ASCII VALUE -- 65 to 90
# 0 to 9 ASCII VALUE -- 48 to 57

# print(ord('m'))
# print(chr(90))
 
# l.sort()
# l.sort(reverse=True)
l.sort(key=len,reverse=True)
# print(l)