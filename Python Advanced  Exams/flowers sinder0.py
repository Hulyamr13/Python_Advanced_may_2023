from collections import deque

def check_word(char, word):
    if char in word:
        word = word.replace(char, "")
    return word


flowers = ["rose", "tulip", "lotus", "daffodil"]
found_word = False

vowels = deque(input().split())
consonants = input().split()

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()
    flowers = [check_word(vowel, flower) for flower in flowers]
    flowers = [check_word(consonant, flower) for flower in flowers]
    if any(flower == '' for flower in flowers):
        found_word = True
        break

if not found_word:
    print("Cannot find any word!")
else:
    found_index = flowers.index("")
    if found_index == 0:
        print("Word found: rose")
    elif found_index == 1:
        print("Word found: tulip")
    elif found_index == 2:
        print("Word found: lotus")
    elif found_index == 3:
        print("Word found: daffodil")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
