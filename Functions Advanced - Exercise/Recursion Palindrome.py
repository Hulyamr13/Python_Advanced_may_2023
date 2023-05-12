def palindrome(word, i=0):
    if i >= len(word) // 2:
        return f"{word} is a palindrome"
    if word[i] != word[-i - 1]:
        return f"{word} is not a palindrome"
    return palindrome(word, i+1)


print(palindrome("abcba", 0))  # abcba is a palindrome
print(palindrome("peter", 0))  # peter is not a palindrome
