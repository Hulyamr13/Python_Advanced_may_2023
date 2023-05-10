class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


input_str = input()
stack = Stack()

for char in input_str:
    stack.push(char)

reversed_str = ""
while not stack.is_empty():
    reversed_str += stack.pop()

print(reversed_str)