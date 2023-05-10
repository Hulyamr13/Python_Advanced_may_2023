# Read integers from input
numbers = input().split()

# Create an empty stack
stack = []

# Push all integers onto the stack
for num in numbers:
    stack.append(num)

# Pop all integers from the stack and print them
while stack:
    print(stack.pop(), end=' ')
