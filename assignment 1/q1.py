# Q1: Sentence Analysis
sentence = input("Enter a sentence: ")

# Number of characters
num_chars = len(sentence)

# Number of words
num_words = len(sentence.split())

# Number of vowels
vowels = 'aeiouAEIOU'
num_vowels = 0
for char in sentence:
    if char in vowels:
        num_vowels += 1

print(f"Number of characters: {num_chars}")
print(f"Number of words: {num_words}")
print(f"Number of vowels: {num_vowels}")
