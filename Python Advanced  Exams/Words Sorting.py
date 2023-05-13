def words_sorting(*words):
    word_dict = {}
    total_sum = 0
    for word in words:
        word_sum = sum(ord(c) for c in word)
        word_dict[word] = word_sum
        total_sum += word_sum
    if total_sum % 2 == 0:
        sorted_dict = dict(sorted(word_dict.items()))
    else:
        sorted_dict = dict(sorted(word_dict.items(), key=lambda x: x[1], reverse=True))
    return '\n'.join([f"{k} - {v}" for k, v in sorted_dict.items()])


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
