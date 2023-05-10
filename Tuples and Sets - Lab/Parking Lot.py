from collections import deque

n = int(input())
parking_lot = deque()

for i in range(n):
    direction, car_number = input().split(", ")
    if direction == "IN":
        if car_number not in parking_lot:
            parking_lot.append(car_number)
    else:
        if car_number in parking_lot:
            parking_lot.remove(car_number)

if parking_lot:
    print("\n".join(parking_lot))
else:
    print("Parking Lot is Empty")
