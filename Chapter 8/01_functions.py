def avg():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = int(input("Enter one more number: "))

    average = (a + b + c) / 3
    return average

print("The average of the three numbers is:", avg())