import re

def resolver(condition, current_value, next_value):
    return current_value if condition == "t" else next_value

def evaluate_expression(expr):
    while True:
        expression = re.findall(r"[tf] \? \d+ : \d+", expr)
        if not expression:
            break
        for e in expression:
            condition, first, second = e.split()[0::2]
            answer = resolver(condition, first, second)
            expr = expr.replace(e, answer)
    return expr

line = input()
result = evaluate_expression(line)
print(result)
