# Ask the user to provide a line of text.
# Scan the text for the following mildly offensive words: \
# arse, bloody, damn, dummy.
# If you find any, then replace its letters with asterisks \
# except for the first letter in each offensive word.
# Print the resulting text.


text = input("Enter a line of text: ")
text = text.lower()
text = text.replace("arse", "a***")
text = text.replace("bloody", "b*****")
text = text.replace("damn", "d***")
text = text.replace("dummy", "d****")
print(text)