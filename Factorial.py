def factorial(x):
    if x==0:
        return 1
    else:
        return x*factorial(x-1)
    
def menu():
    print("SUPER BEAUTIFUL FACTORIAL CALCULATOR")
    print("------------------------------------")
    x = int(input("Enter a number: "))
    result = factorial(x)
    print("------------------------------------")
    print(f"The factorial of {x} is {result}")

menu()