import re

valid_reservation_pattern = r'^\S{8}$'

regular, vip = set(), set()

for i in range(int(input())):
    res = input()
    if re.findall(valid_reservation_pattern, res):
        if res[0].isdigit():
            vip.add(res)
        else:
            regular.add(res)

while True:
    res = input()
    if res == "END":
        break
    elif res in regular:
        regular.remove(res)
    elif res in vip:
        vip.remove(res)

print(len(vip)+len(regular))
print('\n'.join(sorted(vip)))
print('\n'.join(sorted(regular)))
