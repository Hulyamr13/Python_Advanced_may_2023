n = int(input())
petrol_pumps = []
for i in range(n):
    petrol, distance = map(int, input().split())
    petrol_pumps.append((petrol, distance))

start = 0  # starting petrol pump
petrol_in_tank = 0  # current petrol in tank
petrol_needed = 0  # petrol needed to reach the next petrol pump

for i in range(n):
    petrol, distance = petrol_pumps[i]
    petrol_in_tank += petrol
    petrol_needed += distance
    if petrol_in_tank < petrol_needed:
        # cannot reach the next petrol pump
        start = i + 1
        petrol_in_tank = 0
        petrol_needed = 0

print(start)