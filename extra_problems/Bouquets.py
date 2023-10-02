from collections import deque

input1 = input()
input2 = input()

tulips = deque(map(int, input1.split(', ')))
daffodils = deque(map(int, input2.split(', ')))

counter = 5
left = 0

while (daffodils and tulips) or counter > 5:
    single_tulips = tulips.pop()
    single_daffodils = daffodils.popleft()
    while True:
        if single_tulips + single_daffodils < 15:
            left += single_tulips + single_daffodils
            break
        elif single_tulips + single_daffodils == 15:
            counter -= 1
            break
        else:
            single_tulips -= 2

counter -= left // 15

if counter <= 0:
    print("You made it! You go to the competition with 5 bouquets!")
else:
    print(f"You failed... You need more {counter} bouquets.")
