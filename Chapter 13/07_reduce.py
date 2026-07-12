from functools import reduce

numbers = [1,2,3,4,5]

result = reduce(lambda x,y:x+y,numbers)

print(result)


from functools import reduce

numbers = [2,3,4]

result = reduce(lambda x,y:x*y,numbers)

print(result)