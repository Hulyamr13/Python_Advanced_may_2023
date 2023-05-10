# Get input string from user
input_str = input()

# Use a stack to reverse the string
stack = list(input_str)
output_str = ""
while stack:
    output_str += stack.pop()

# Print the reversed string
print(output_str)
