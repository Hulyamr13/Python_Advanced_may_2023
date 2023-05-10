from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

cars = deque()
crashed = False
total_cars_passed = 0

while not crashed:
    command = input()

    if command == "green":
        time_left = green_light_duration

        while time_left > 0 and cars:
            car = cars.popleft()
            time_left -= len(car)

            if time_left >= 0:
                total_cars_passed += 1
            else:
                free_window_left = abs(time_left)

                if free_window_left <= free_window_duration:
                    total_cars_passed += 1
                else:
                    crashed = True
                    print("A crash happened!")
                    print(f"{car} was hit at {car[free_window_duration + time_left]}.")
                    break
    elif command == "END":
        print("Everyone is safe.")
        print(f"{total_cars_passed} total cars passed the crossroads.")
        break
    else:
        cars.append(command)
