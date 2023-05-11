size = int(input())
matrix = [list(map(int, input().split(", "))) for _ in range(size)]

primary_diagonal = [matrix[i][i] for i in range(size)]
secondary_diagonal = [matrix[i][size - 1 - i] for i in range(size)]

primary_sum = sum(primary_diagonal)
secondary_sum = sum(secondary_diagonal)

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {primary_sum}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {secondary_sum}")