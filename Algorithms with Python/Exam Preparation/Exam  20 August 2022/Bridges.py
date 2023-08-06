def main():
    bridges = list(map(int, input().split()))
    found = []
    last = 0

    for i in range(len(bridges)):
        for j in range(last, i):
            start = bridges[j]
            end = bridges[i]
            if start == end:
                found.append(j)
                found.append(i)
                last = i
                break

    result = ['X'] * len(bridges)
    for index in found:
        result[index] = str(bridges[index])

    if not found:
        print("No bridges found")
        print(' '.join(result))
    elif len(found) // 2 == 1:
        print("1 bridge found")
        print(' '.join(result))
    else:
        print(f"{len(found) // 2} bridges found")
        print(' '.join(result))

if __name__ == "__main__":
    main()
