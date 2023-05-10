parentheses = input()

stack = []

for p in parentheses:
    if p in ['(', '[', '{']:
        stack.append(p)
    elif p in [')', ']', '}']:
        if len(stack) == 0:
            print("NO")
            exit()
        elif (p == ')' and stack[-1] != '(') or (p == ']' and stack[-1] != '[') or (p == '}' and stack[-1] != '{'):
            print("NO")
            exit()
        else:
            stack.pop()

if len(stack) == 0:
    print("YES")
else:
    print("NO")