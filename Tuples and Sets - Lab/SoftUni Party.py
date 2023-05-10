n = int(input())
vip_guests = set()
regular_guests = set()

for i in range(n):
    reservation_code = input()
    if reservation_code[0].isdigit():
        vip_guests.add(reservation_code)
    else:
        regular_guests.add(reservation_code)

guest = input()
while guest != "END":
    if guest in vip_guests:
        vip_guests.remove(guest)
    elif guest in regular_guests:
        regular_guests.remove(guest)
    guest = input()

vip_guests_not_attending = sorted(vip_guests)
regular_guests_not_attending = sorted(regular_guests)

print(len(vip_guests) + len(regular_guests))
for vip in vip_guests_not_attending:
    print(vip)
for regular in regular_guests_not_attending:
    print(regular)
