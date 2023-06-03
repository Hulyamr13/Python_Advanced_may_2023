class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return False if self.data else True

    def __str__(self):
        return '[' + ', '.join(self.data[::-1]) + ']'


stack = Stack()
stack.push("element1")
stack.push("element2")
stack.push("element3")
print(stack)  # Output: [element3, element2, element1]
print(stack.pop())  # Output: element3
print(stack.top())  # Output: element2
print(stack.is_empty())  # Output: False
