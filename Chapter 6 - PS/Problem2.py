# 2. Pass or fail
sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))

total_percentage = (sub1 + sub2 + sub3) / 3

if total_percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
    print("Pass")
else:
    print("Fail")