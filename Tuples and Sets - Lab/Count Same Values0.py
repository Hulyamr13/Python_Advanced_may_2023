numbers = input().split()
count = {}

for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

for num, freq in count.items():
    print(f"{float(num):.1f} - {freq} times")
