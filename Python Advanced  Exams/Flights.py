def flights(*args):
    flight_dict = {}
    while True:
        flights = args[:2]
        if flights[0] == 'Finish':
            break
        if flights[0] not in flight_dict:
            flight_dict[flights[0]] = flights[1]
        else:
            flight_dict[flights[0]] += flights[1]
        args = args[2:]
    return flight_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))