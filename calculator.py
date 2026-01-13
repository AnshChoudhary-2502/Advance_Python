import square
import time

def Time_taken(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")
    return wrapper

@Time_taken
def Calculator():
    sign = input("What operation do you want to perform? (add, subtract, multiply, divide, square): ")

    if sign == "+":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(a + b)
    elif sign == "-":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(a - b)
    elif sign == "x":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(a * b)
    elif sign == "/":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(a / b)
    elif sign == "*":
        a = int(input("Enter number to square: "))
        result = square.square(a)
        print(result)
    else:
        print("Invalid operation")

Calculator()