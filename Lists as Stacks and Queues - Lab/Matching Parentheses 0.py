class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


expression = input()
stack = Stack()

for i in range(len(expression)):
    if expression[i] == "(":
        stack.push(i)
    elif expression[i] == ")":
        start_index = stack.pop()
        print(expression[start_index:i+1])