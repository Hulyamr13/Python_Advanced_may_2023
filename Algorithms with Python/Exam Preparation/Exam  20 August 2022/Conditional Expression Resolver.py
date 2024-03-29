import re


def resolver(condition, current_value, next_value):
    return current_value if condition == "t" else next_value


line = input()
pattern = r"[tf] \? \d+ : \d+"

while True:
    expression = re.findall(pattern, line)
    if not expression:
        break
    for e in expression:
        condition, first, second = e.split()[0::2]
        answer = resolver(condition, first, second)
        line = line.replace(e, answer)

print(line)
