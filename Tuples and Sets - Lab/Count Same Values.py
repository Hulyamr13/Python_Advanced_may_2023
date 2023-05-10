from collections import Counter

numbers = input().split()
count = Counter(numbers)

for num, freq in count.items():
    print(f"{float(num):.1f} - {freq} times")