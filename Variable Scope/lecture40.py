# def func():
#     a = 50
#     print(a)

# # func()
# print(a)

# a = 5
# # a += 5
# print(a)

# def func():
#     global a
#     a += 5
#     print(a)

# func()

def func():
    a = 50
    def printa():
        nonlocal a
        a+=10
        print(a)
    printa()

func()
