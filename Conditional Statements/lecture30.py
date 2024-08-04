# ------------------ Ques - 1 ----------------------------

# a = eval(input("Enter your value : "))

# if isinstance(a,str):
#     print("Input is of type string and ")
#     print(len(a))
# elif isinstance(a,list):
#     print("Input is of type list and ")
#     print(a)
#     a.pop()
#     print(a)
# elif isinstance(a,tuple):
#     print("Input is of type tuple and ")
#     print(a[::-1])
# else:
#     print("Invalid Input")

# ------------------ Ques - 2 ----------------------------

num = int(input("Enter the number : "))

if num%2!=0:
    print("Number is odd")
    if num%7==0:
        print("and number is divisible by 7")
    else:
        print("and number is not divisible by 7")
else:
    print("Number is even")