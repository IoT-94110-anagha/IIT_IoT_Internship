def greet(name="Anagha", msg="welcome"):
    print(msg, name)

greet()
greet("sonali")
greet(name="sonali", msg="Hello")
    
def add(a,b):
    return a+b
def mul(a,b):
    return a*b

def function(func,a,b):
    return func(a,b)
   
print( "Addition:",function(add,12,13))
print("Multiplication:",function(mul,12,13))
