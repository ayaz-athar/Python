a = int(input("Enter your age: "))
if (a>=18):
    print("You are eligible to vote")
elif (a<0):
    print("You have entered an invalid age")
else:
    print("You are not eligible to vote")
    print(a)