from math import floor

expression = input().split()
result = 0

while len(expression) > 1:
    index = None
    for i, item in enumerate(expression):
        if item in ['*', '+', '/', '-']:
            index = i
            break

    if index is None:
        break

    sentence = list(map(int, expression[:index]))
    operation = expression[index]
    expression = expression[index + 1:]

    if operation == '*':
        result = 1
        for item in sentence:
            result *= item
    elif operation == '+':
        result = sum(sentence)
    elif operation == '/':
        result = sentence[0]
        for item in sentence[1:]:
            result /= item
    elif operation == '-':
        result = sentence[0]
        for item in sentence[1:]:
            result -= item

    expression.insert(0, result)

print(floor(result))