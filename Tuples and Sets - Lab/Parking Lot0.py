n = int(input())
parking_lot = set()

for _ in range(n):
    direction, car_number = input().split(", ")
    if direction == "IN":
        parking_lot.add(car_number)
    elif direction == "OUT":
        if car_number in parking_lot:
            parking_lot.remove(car_number)

if parking_lot:
    print("\n".join(parking_lot))
else:
    print("Parking Lot is Empty")
