from collections import deque

words = ["pear", "flour", "pork", "olive"]
found_words = ["****", "*****", "****", "*****"]

vowels = deque(input().split())
consonants = deque(input().split())

while consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for i, word in enumerate(words):
        index_vowel = word.find(vowel)
        index_consonant = word.find(consonant)

        if index_vowel >= 0:
            found_words[i] = found_words[i][:index_vowel] + vowel + found_words[i][index_vowel + 1:]

        if index_consonant >= 0:
            found_words[i] = found_words[i][:index_consonant] + consonant + found_words[i][index_consonant + 1:]

    vowels.append(vowel)

output = [w for w in found_words if "*" not in w]

print(f"Words found: {len(output)}")
print("\n".join(output))
