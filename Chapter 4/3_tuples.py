a=(5,6,7,8)
b=(1,2,3,4)
print(a+b) #concatenation of tuples
print(a*3) #repetition of tuples
print(a[1:3]) #slicing of tuples
print(type(a)) #type of tuple
print(len(a)) #length of tuple
# a[0]=10 #tuples are immutable, this will raise an error
a.count(5) #count method returns the number of occurrences of a specified element in the tuple
print(a.count(5))
a.index(7) #index method returns the index of the first occurrence of a specified element in the tuple
print(a.index(7))