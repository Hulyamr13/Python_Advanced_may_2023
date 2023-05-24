from collections import Counter

def word_count(words_file, text_file, output_file):
    with open(words_file, 'r') as f:
        words = f.read().split()

    with open(text_file, 'r') as f:
        text = f.read()

    text = text.lower()

    word_counts = Counter(word.lower() for word in words)
    for word in word_counts:
        count = text.count(word)
        word_counts[word] = count

    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    with open(output_file, 'w') as f:
        for word, count in sorted_words:
            f.write(f'{word} - {count}\n')

word_count('words.txt', 'text.txt', 'output.txt')
