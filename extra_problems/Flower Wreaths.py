from collections import deque

input1 = input()
input2 = input()

lilies = deque(map(int, input1.split(", ")))
roses = deque(map(int, input2.split(", ")))

counter = 5
left = 0

while (roses and lilies) or counter > 5:
    single_tulips = lilies.pop()
    single_daffodils = roses.popleft()

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
    print("You made it, you are going to the competition with 5 wreaths!")
else:
    print("You didn't make it, you need " + str(counter) + " wreaths more!")
