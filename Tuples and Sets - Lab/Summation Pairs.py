numbers = input().split()
target = int(input())
hash_table = {}

for num in numbers:
    num = int(num)
    diff = target - num
    if diff in hash_table:
        print(f"{diff} + {num} = {target}")
    else:
        hash_table[num] = True
