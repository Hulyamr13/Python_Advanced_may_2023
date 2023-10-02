from collections import deque

tasks = deque(int(x) for x in input().split(', '))
interested_task_ind = int(input())
clocks = 0

while tasks:
    current_task = min([x for x in tasks if x !=0])
    current_task_ind = tasks.index(current_task)

    if current_task_ind == interested_task_ind:
        clocks += current_task
        break

    clocks += current_task
    tasks[current_task_ind] = 0

print(clocks)