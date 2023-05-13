jobs = [int(x) for x in input().split(', ')]
searched_idx = int(input())

clock_cycles = 0

while True:
    task = min(jobs)
    clock_cycles += task
    if jobs.index(task) == searched_idx:
        break
    jobs[jobs.index(task)] = float('inf')

print(clock_cycles)
