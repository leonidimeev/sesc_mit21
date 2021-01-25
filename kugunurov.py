print("Calculator!")
while True:
    x = int(input("Number 1: "))
    y = int(input("Number 2: "))
    operation = input("Choose operation:\n+\n-\n*\n:\n%\n")
    if operation == "+":
        print(x+y)
    if operation == "-":
        print(x-y)
    if operation == "*":
        print(x*y)
    if operation == ":":
        print(x//y)
    if operation == "%":
        print(x%y)