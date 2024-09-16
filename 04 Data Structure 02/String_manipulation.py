
text = input("Enter a string :")

substring = input("Enter a substring : ")
index = text.find(substring)  # Returns 6
indices = [i for i in range(len(text)) if text.startswith(substring, i)]
print(indices)
new_text = text.replace("world", "there", 1)
print(new_text)
new_text = text.replace("world", "there")
print("All occurence :",new_text)

#----------------------------------------------------------------

#Assignment Replacing alternative words
paragraph = "A single string paragraph that represents a paragraph of text."
words = paragraph.split()
for i in range(1, len(words), 2):
    words[i] = "replaced"
new_paragraph = ' '.join(words)
print(new_paragraph)