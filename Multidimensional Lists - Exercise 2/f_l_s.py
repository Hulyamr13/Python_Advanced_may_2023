print(*[num for sublist in input().split('|')[::-1] for num in map(int, sublist.strip().split()) if sublist.strip()])