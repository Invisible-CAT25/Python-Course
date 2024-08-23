# Ques-1

# s = "python123"
# vowel = []
# num = []

# for i in s:
#     if i in "aeiou":
#         vowel.append(i)
#     if i in "0123456789":
#         num.append(i)

# print(vowel)
# print(num)

# Ques-2
# a = [12,False,True,56.7,3+5j,"python",(1,2,3,4),[1,2,3,4],{1,5,7},56,90,5+7j]
# sum = 0

# for i in a:
#     if isinstance(i,(int,float,complex,bool)):
#         sum += i

# print(sum)

# Ques-3
s = "hello123python456programming789"
sum = 0

for i in s:
    if i in "0123456789":
        sum += int(i)

print(sum)