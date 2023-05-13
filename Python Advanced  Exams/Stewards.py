from collections import deque

seats = input().split(", ")
first_numbers = deque(map(int, input().split(", ")))
second_numbers = deque(map(int, input().split(", ")))
rotations = 0
taken_seats = []

while rotations < 10 and len(taken_seats) < 3 and first_numbers and second_numbers:
    first_number, second_number = first_numbers.popleft(), second_numbers.pop()
    sum_of_both_numbers = first_number + second_number
    ascii_char = chr(sum_of_both_numbers)
    for seat in [f"{first_number}{ascii_char}", f"{second_number}{ascii_char}"]:
        if seat in taken_seats or seat not in seats:
            continue
        seats.remove(seat)
        taken_seats.append(seat)
        break
    else:
        first_numbers.append(first_number)
        second_numbers.appendleft(second_number)
    rotations += 1

print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations}")
