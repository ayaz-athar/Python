try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError:
    print("Invalid input. Please enter a valid integer.")
except Exception as e:
    print(e)


else:
    print("No exception occurred. The input was valid.")