def forecast(*locations):
    sunny = []
    cloudy = []
    rainy = []

    for location in locations:
        if location[1] == "Sunny":
            sunny.append(location[0])
        elif location[1] == "Cloudy":
            cloudy.append(location[0])
        else:
            rainy.append(location[0])

    sunny.sort()
    cloudy.sort()
    rainy.sort()

    sorted_locations = []

    sorted_locations.extend([(location, "Sunny") for location in sunny])
    sorted_locations.extend([(location, "Cloudy") for location in cloudy])
    sorted_locations.extend([(location, "Rainy") for location in rainy])

    return "\n".join([f"{location} - {weather}" for (location, weather) in sorted_locations])


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
