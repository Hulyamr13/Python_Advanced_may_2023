from collections import deque

registration_plate_as_queue = deque(map(int, input().split(", ")))
cars_as_stack = deque(map(int, input().split(", ")))

count_of_registered_cars = 0
count_of_installation_days = 0

while registration_plate_as_queue and cars_as_stack:
    count_of_installation_days += 1
    current_number_of_plate = registration_plate_as_queue.popleft()
    curr_number_of_cars = cars_as_stack.pop()

    if current_number_of_plate > (curr_number_of_cars * 2):
        registration_plate_as_queue.append(current_number_of_plate - (curr_number_of_cars * 2))
        count_of_registered_cars += curr_number_of_cars
    elif current_number_of_plate < (curr_number_of_cars * 2):
        left_cars = curr_number_of_cars - (current_number_of_plate // 2)
        cars_as_stack.append(left_cars)
        count_of_registered_cars += (current_number_of_plate // 2)
    else:
        count_of_registered_cars += curr_number_of_cars

print(f"{count_of_registered_cars} cars were registered for {count_of_installation_days} days!")
if registration_plate_as_queue:
    sum_of_unplaced_plates = sum(registration_plate_as_queue)
    print(f"{sum_of_unplaced_plates} license plates remain!")
elif cars_as_stack:
    sum_of_cars_without_plate = sum(cars_as_stack)
    print(f"{sum_of_cars_without_plate} cars remain without license plates!")
else:
    print("Good job! There is no queue in front of the KAT!")
