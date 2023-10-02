from collections import deque

input1 = input()
input2 = input()

magic_box_one = deque(map(int, input1.split()))
magic_box_two = deque(map(int, input2.split()))

sum = 0
while magic_box_one and magic_box_two:
    if (magic_box_one[0] + magic_box_two[-1]) % 2 == 0:
        sum += magic_box_one.popleft() + magic_box_two.pop()
    else:
        magic_box_one.append(magic_box_two.pop())

if not magic_box_one:
    print("First magic box is empty.")
else:
    print("Second magic box is empty.")

if sum >= 90:
    print(f"Wow, your prey was epic! Value: {sum}")
else:
    print(f"Poor prey... Value: {sum}")
