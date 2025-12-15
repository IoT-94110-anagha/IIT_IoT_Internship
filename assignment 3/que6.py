    
def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b

def cal(func,a,b):
    return func(a,b)

a=int(input("enter num:"))
b=int(input("enter num:"))
print(cal(add,a,b))
print(cal(sub,a,b))
print(cal(mul,a,b))
print(cal(div,a,b))