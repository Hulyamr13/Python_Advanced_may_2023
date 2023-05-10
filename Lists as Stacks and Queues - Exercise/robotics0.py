# read robots
robotics = input().split(";")
robots = {}
for name_seconds in robotics:
    name, seconds = name_seconds.split('-')
    robots[name] = int(seconds)

# set available robots
available_robots = list(robots.keys())

# read starting time
starting_time_parts = [int(num) for num in input().split(':')]
time_seconds = starting_time_parts[0] * 3600 + starting_time_parts[1] * 60 + starting_time_parts[2]

# read products
products = []
product = input()
while product != "End":
    products.append(product)
    product = input()

# process products
processing_robots = {}
while len(products) > 0 or len(processing_robots) > 0:
    time_seconds += 1
    if time_seconds >= 24 * 60 * 60:
        time_seconds -= 24 * 60 * 60

    robots_to_remove = []
    for robot_name in processing_robots:
        processing_robots[robot_name] -= 1
        if processing_robots[robot_name] == 0:
            robots_to_remove.append(robot_name)
    for robot_name in robots_to_remove:
        del processing_robots[robot_name]

    if len(products) > 0:
        current_product = products[0]
        for robot in available_robots:
            if robot not in processing_robots:
                processing_robots[robot] = robots[robot]
                print(f"{robot} - {current_product} [{time_seconds // 3600:02d}:{time_seconds // 60 % 60:02d}:{time_seconds % 60:02d}]")
                products.pop(0)
                break
        else:
            products.append(products.pop(0))