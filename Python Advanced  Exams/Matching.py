males = [int(x) for x in input().split()]
females = [int(x) for x in input().split()]

matches = 0

while males and females:
    females = [female for female in females if female > 0]
    males = [male for male in males if male > 0]

    if not males or not females:
        break

    if females[0] % 25 == 0:
        females.pop(0)
        if females:
            females.pop(0)
        continue

    if males[-1] % 25 == 0:
        males.pop()
        if males:
            males.pop()
        continue

    female = females.pop(0)
    male = males.pop()

    if female == male:
        matches += 1
    else:
        males.append(male - 2)

print(f"Matches: {matches}")
print(f"Males left: {'none' if not males else ', '.join(str(x) for x in reversed(males))}")
print(f"Females left: {'none' if not females else ', '.join(str(x) for x in females)}")
