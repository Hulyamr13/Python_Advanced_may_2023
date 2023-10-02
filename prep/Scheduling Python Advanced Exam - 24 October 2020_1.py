jobs = [int(job) for job in input().split(', ')]
index = int(input())
cycles = 0
current_index = -1

while current_index != index:
    current_index = jobs.index(min(jobs))  # first occurrence of the min amount of clock cycles
    current_job = min(jobs)  # take the amount of min clock cycles
    jobs[current_index] = max(jobs) + 1  # set element on current index to max + 1 to not get processed again
    cycles += current_job  # add the clock cycles
print(cycles)