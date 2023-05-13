from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())
words = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}
found_word = False

while vowels and consonants:
    v = vowels.popleft()
    c = consonants.pop()
    words = {word: words[word].replace(v, '').replace(c, '') for word in words.keys()}
    if any(val == '' for val in words.values()):
        word = [word for word in words.keys() if words[word] == ''][0]
        print(f"Word found: {word}")
        found_word = True
        break

if not found_word:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
