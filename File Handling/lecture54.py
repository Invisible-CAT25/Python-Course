# f = open("sample1.txt",'a')
# # f = open(r"C:\Users\gargj\Desktop\Python-Course\sample.txt")
# # print(f.readable())
# f.write("this is my")
# f.close()

with open("sample.txt",'a+') as abcd:
    print(abcd.read())