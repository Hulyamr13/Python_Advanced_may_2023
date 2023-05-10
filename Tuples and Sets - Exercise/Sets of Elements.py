n, m = map(int, input().split())

set1 = set()
set2 = set()

for i in range(n):
    num = int(input())
    set1.add(num)

for i in range(m):
    num = int(input())
    set2.add(num)

common_elements = set1.intersection(set2)

for element in common_elements:
    print(element)