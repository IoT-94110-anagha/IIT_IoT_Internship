def fact(n):
    if(n==1):
        return 1
    return n*fact(n-1)
def power(n,p):
    if(p==0):
        return 1
    return n*power(n,p-1)
n=int(input("enter num:"))
p=int(input("enter power:"))
print("fact:",fact(n))
print("power:",power(n,p))