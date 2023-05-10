clothes = list(map(int, input().split()))
rack_capacity = int(input())

total_sum = 0
racks_used = 1
stack = []

for cloth in reversed(clothes):
    if total_sum + cloth > rack_capacity:
        racks_used += 1
        total_sum = cloth
        stack.clear()
    else:
        total_sum += cloth
    stack.append(cloth)

print(racks_used)