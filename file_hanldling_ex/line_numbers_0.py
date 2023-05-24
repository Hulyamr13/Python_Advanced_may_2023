def count_letters_and_punctuation(line):
    letter_count = sum(1 for char in line if char.isalpha())
    punctuation_count = sum(1 for char in line if char in '.,!?')

    return letter_count, punctuation_count


def process_text_file(input_file, output_file):
    with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
        lines = input_f.readlines()

        for i, line in enumerate(lines, start=1):
            line = line.strip()
            letter_count, punctuation_count = count_letters_and_punctuation(line)

            output_line = f"Line {i}: {line} ({letter_count})({punctuation_count})\n"
            output_f.write(output_line)


process_text_file("files/text.txt", "files/output.txt")
