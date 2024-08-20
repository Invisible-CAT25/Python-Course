# # Armstrong Number

# # a = 1234
# num = int(input("Enter a Number : "))
# # print(num)
# temp = num
# # print(type(num))
# # print(len(num))
# length = len(str(num))
# # print(length)
# arm = 0
# while num!=0:
#     arm += (num%10)**length
#     num //= 10

# # print(num)
# if arm==temp:
#     print("Number is a armstrong number")
# else:
#     print("Number is not a armstrong number")

# # a = 1234
# # print(a%10)
# # print(1234//10)

# Strong Number
num = 5
fact = 1

while num>0:
    fact = fact * num
    num = num - 1

print(fact)