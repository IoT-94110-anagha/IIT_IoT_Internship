def overlapping(l1,l2):
    for item in l1:
        if item in l2:
            return True
    return False
l1=list(map(int,input("enter list 1:").split()))
l2=list(map(int,input("enter list 2:").split()))
print("list1",l1)
print("list2",l2)
result=overlapping(l1,l2)
print(result)