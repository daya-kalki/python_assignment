word = input("Enter the word: ")
vowels = []
consonants = []
for char in word:
    if char.lower() in 'aeiou':
        vowels.append(char.upper())
    elif char.isalpha():
        consonants.append(char.upper())
vowels.sort()
consonants.sort()
print("Vowels in alphabetical order:", ", ".join(vowels))
print("Consonants in alphabetical order:", ", ".join(consonants))
if len(vowels) > len(consonants):
    print("Maximum Count: Vowels")
elif len(consonants) > len(vowels):
    print("Maximum Count: Consonants")
else:
    print("Maximum Count: Equal")
