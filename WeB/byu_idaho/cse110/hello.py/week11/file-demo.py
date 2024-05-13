wddtext = open("cus.txt")
for line in "wddtext":
    print('line')
wddtext.close()

with open("cus.txt") as cus_file:
    for line in cus_file:
        print(line)


sentence = "I will go and do"

words = sentence.split(" ")
# The variable "words" is now a list that contains each word.

# You can iterate through each word and do something with it, such as display it:
for word in words:
    print(word)

line = "  j   text"

line = line.strip()

print(line)
with open("books.txt") as book_file:
    for line in book_file:
        book = line.strip()
        print(book)