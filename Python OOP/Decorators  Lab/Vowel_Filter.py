def vowel_filter(func):
    def wrapper():
        letters = func()
        vowels = [letter for letter in letters if letter.lower() in 'aeiou']
        return vowels
    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
