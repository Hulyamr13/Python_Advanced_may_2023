n = int(input())

odd_set = set()
even_set = set()

for i in range(1, n + 1):
    name = input()
    ascii_sum = sum(ord(ch) for ch in name)
    division_result = ascii_sum // i

    if division_result % 2 == 0:
        even_set.add(division_result)
    else:
        odd_set.add(division_result)

sum_odd = sum(odd_set)
sum_even = sum(even_set)

if sum_odd == sum_even:
    print(", ".join(str(x) for x in odd_set.union(even_set)))
elif sum_odd > sum_even:
    print(", ".join(str(x) for x in odd_set.difference(even_set)))
else:
    print(", ".join(str(x) for x in odd_set.symmetric_difference(even_set)))