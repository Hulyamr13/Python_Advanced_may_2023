stack = []
max_stack = []
min_stack = []

# Read number of queries
n = int(input())

for i in range(n):
    query = input().split()

    if query[0] == '1':
        num = int(query[1])
        stack.append(num)
        if not max_stack or num >= max_stack[-1]:
            max_stack.append(num)
        if not min_stack or num <= min_stack[-1]:
            min_stack.append(num)

    elif query[0] == '2':
        if stack:
            num = stack.pop()
            if num == max_stack[-1]:
                max_stack.pop()
            if num == min_stack[-1]:
                min_stack.pop()

    elif query[0] == '3':
        if max_stack:
            print(max_stack[-1])

    elif query[0] == '4':
        if min_stack:
            print(min_stack[-1])

# Print the final stack from top to bottom
stack.reverse()
print(", ".join(str(num) for num in stack))
