# 3. Spam comment detector
comment = input("Enter comment: ")

spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]

if comment.lower() in spam_keywords:
    print("Spam comment")
else:
    print("Not spam")