def square(x):
    return x*x

print(square(5))

add = lambda a, b: a+b

print(add(10,20))

students = [
    ("Ayaz",80),
    ("Ali",95),
    ("Ahmed",70)
]

students.sort(key=lambda x:x[1])

print(students)