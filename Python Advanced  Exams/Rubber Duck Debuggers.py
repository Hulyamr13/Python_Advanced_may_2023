programmer_time = list(map(int, input().split()))
tasks = list(map(int, input().split()))

dv_count = th_count = bb_count = sy_count = 0

while tasks:
    time = programmer_time[0] * tasks[-1]
    if time <= 60:
        dv_count += 1
    elif time <= 120:
        th_count += 1
    elif time <= 180:
        bb_count += 1
    elif time <= 240:
        sy_count += 1
    else:
        tasks[-1] -= 2
        programmer_time.append(programmer_time.pop(0))
        continue
    tasks.pop()
    programmer_time.pop(0)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {dv_count}")
print(f"Thor Ducky: {th_count}")
print(f"Big Blue Rubber Ducky: {bb_count}")
print(f"Small Yellow Rubber Ducky: {sy_count}")
