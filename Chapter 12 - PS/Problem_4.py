try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    print("Result =", a / b)

except ZeroDivisionError:
    print("Infinite")