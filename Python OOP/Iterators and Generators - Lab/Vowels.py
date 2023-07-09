class vowels:
    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        vowels = 'aeiouAEIOU'
        while self.index < len(self.string):
            current_char = self.string[self.index]
            self.index += 1
            if current_char in vowels:
                return current_char
        raise StopIteration

# Example usage
my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
