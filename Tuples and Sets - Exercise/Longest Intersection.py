n = int(input())

longest_intersection = set()

for i in range(n):
    first_range, second_range = input().split('-')
    start_1, end_1 = map(int, first_range.split(','))
    start_2, end_2 = map(int, second_range.split(','))
    range_1 = set(range(start_1, end_1 + 1))
    range_2 = set(range(start_2, end_2 + 1))
    intersection = range_1.intersection(range_2)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is [{', '.join(map(str, sorted(longest_intersection)))}] "
      f"with length {len(longest_intersection)}")