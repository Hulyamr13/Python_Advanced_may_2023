n = int(input())

fibonacci = [0, 1]

while len(fibonacci) < n + 2:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(fibonacci[-1])
