def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b if b != 0 else "Division by zero not allowed"

while True:
    print("\n1.Add  2.Subtract  3.Multiply  4.Divide  5.Exit")
    choice = int(input("Enter choice: "))


    match choice:
        case 1:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result =", add(a, b))

        case 2:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result =", sub(a, b))

        case 3:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result =", mul(a, b))

        case 4:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result =", div(a, b))

        case 5:
            print("Exiting calculator...")
            break

        case _:
            print("Invalid choice! Please try again.")