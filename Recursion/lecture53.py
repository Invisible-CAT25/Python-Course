# 5! = 5*4*3*2*1
# 5! = 5*4!
# 5! = 5*4*3!
# 5! = 5*4*3*2!
# 5! = 5*4*3*2*1

def fact(num):
    # base case
    if num==1 or num==0:
        return 1
    # recursive call
    factorial = num*fact(num-1)
    return factorial

print(fact(10))