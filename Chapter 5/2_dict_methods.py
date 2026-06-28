marks = {
    "Harry": 90,
    "Ron": 78,
    "Hermione": 95,
    0:"Harry",
}

print(marks.items()) #prints the dictionary items as a list of tuples
print(marks.keys()) #prints the dictionary keys as a list
print(marks.values()) #prints the dictionary values as a list
print(marks.get("Harry")) #prints the value of the key "Harry"  
print(marks.get("Draco")) #prints None as the key "Draco" is not present in the dictionary
print(marks.update({"Draco": 80})) #adds the key "Draco" with value 80 to the dictionary
print(marks) #prints the updated dictionary