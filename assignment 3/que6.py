    
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
print("Addition:",cal(add,a,b))
print("substraction:",cal(sub,a,b))
print("Multiplication:",cal(mul,a,b))
print("Division:",cal(div,a,b))