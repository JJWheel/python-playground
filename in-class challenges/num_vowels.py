vowels = ('AEIOU')
sentence = input('give me some vowels and ill count them')
sentence = sentence.upper()
num_vowel = 0
# print(sentence)
for char in sentence:
    if char in vowels:
        num_vowel += 1
print(num_vowel)