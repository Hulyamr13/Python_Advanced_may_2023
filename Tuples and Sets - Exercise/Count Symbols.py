text = input()
char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char in sorted(char_count):
    print(char + ': ' + str(char_count[char]) + ' time/s')