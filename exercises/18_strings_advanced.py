# Given a sentence
sentence = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."
print(sentence)

# Count how many vowels are in the sentence

vowels = ["a", "e", "i", "o", "u"]

vowels_no = 0

# counts characters (char)
for char in sentence:
    if char in vowels:
        vowels_no += 1

print(vowels_no)

# Count how many words it contains

no_word = 0

for word in sentence.split():
    no_word +=1

print(no_word)

# Remove all spaces

x = " "

sentence_new = sentence.replace(x, "")

print(sentence_new)

# Replace a specific word with another

new_word = "nichi"
sentence_nichi = sentence.replace("industry", new_word)

print(sentence_nichi)

# Reverse the sentence
sentence_reverse = sentence[::-1]

print(sentence_reverse)





