def remove_and_strip(lst, word):
    new_list = []
    for item in lst:
        if item.strip() != word:
            new_list.append(item.strip())
    return new_list

l = ["Harry", "Rohan", "Shubham", " an "]

print(remove_and_strip(l, "an"))