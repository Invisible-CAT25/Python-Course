# try:
    # a = 10
    # b = 2
    # print(a/c)

    # while True:
    #     print("hello")

# except ZeroDivisionError:
#     print("Error Handled")

# except NameError:
#     print("Handled")

# except AttributeError:
#     print("handled")

# except Exception:
#     print("Handled")

# except:
#     print("handled")

# print("helllo")
# print(a+b)

# class MeraError(Exception):
#     pass

# try:
#     a = 10
#     b = 0

#     if b==0:
#         raise MeraError("Bhai tera b zero hai, isliye error ayega")

# except:
#     print("Handled")

try:
    a = 10
    b = 2
    print(a/b)

except:
    print("Handled")

else:
    print(a*b)

finally:
    print(a+b)