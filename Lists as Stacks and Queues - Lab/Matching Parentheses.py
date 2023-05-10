expression = input()

stack = []
for i, char in enumerate(expression):
    if char == '(':
        stack.append(i)
    elif char == ')':
        start = stack.pop()
        end = i
        print(expression[start:end+1])
