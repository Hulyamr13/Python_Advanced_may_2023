def reverse_words(line):
    line = line.replace("-", "@").replace(",", "@").replace(".", "@").replace("!", "@").replace("?", "@")

    words = line.split()
    words.reverse()
    reversed_line = " ".join(words)

    return reversed_line


def print_even_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        even_lines = [line.strip() for i, line in enumerate(lines) if i % 2 == 0]

        for line in even_lines:
            reversed_line = reverse_words(line)
            print(reversed_line)


print_even_lines("text.txt")
