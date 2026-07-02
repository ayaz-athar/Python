words = {
    "madad": "help",
    "kursi": "chair",
    "mehfil": "room",
    "kitab": "book"
}
word = input("Enter the word you want to translate: ")
print(words.get(word, "Word not found in the dictionary."))