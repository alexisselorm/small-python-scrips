# Get sentence from user
original = input("Enter your sentence: ").strip().lower()
# Split sentence into words
words = original.split()
# Loop through words and convert to pig lating
new_words =[]

#  if word starts with a vowel just add "yay"
for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        # Otherwise move the first consonant cluster to the end and add "ay"
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos += 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word= the_rest + cons + "ay"
        new_words.append(new_word)
    
    # JOIN the words back together
output = " ".join(new_words)
    
    # PRINT the final string
print(output)
