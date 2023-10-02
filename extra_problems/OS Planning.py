from collections import deque

input1 = input()
input2 = input()

tasks = deque(map(int, input1.split(', ')))
threads = deque(map(int, input2.split()))

task_to_kill = int(input())

while True:
    if tasks[0] == task_to_kill:
        print(f'Thread with value {threads[0]} killed task {task_to_kill}')
        break
    elif threads[0] >= tasks[0]:
        tasks.popleft()
        threads.popleft()
    else:
        threads.popleft()

print(' '.join(map(str, threads)))
