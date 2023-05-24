symbols = ["-", ",", ".", "!", "?"]

with open("files/text.txt", "r") as even_lines_file:
    text = even_lines_file.readlines()

for row in range(0, len(text), 2):
    line = text[row].strip()

    for symbol in symbols:
        line = line.replace(symbol, "@")

    words = line.split()
    reversed_words = words[::-1]
    reversed_line = " ".join(reversed_words)
    print(reversed_line)
