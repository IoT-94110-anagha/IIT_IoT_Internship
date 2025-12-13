
def fab(num):
    a = 0
    b=1
    print(a,b ,end=" ")
    for i in range(num):
        c=a+b
        print( c ,end=" ")
        a=b
        b=c
    return c

num = int(input("Enter num : "))

num = fab(num)

