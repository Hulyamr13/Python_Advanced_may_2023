vector = []
numbers = []
count = 0

def main():
    global numbers
    numbers = list(map(int, input().split(' ')))
    generate(0)

def generate(index):
    global count
    number = numbers[index]

    if index == len(numbers) - 1:
        if count == 1:
            return

        vector.append(number)
        print(''.join(str(x) for x in vector))
        vector.pop()
        return

    if number == 1 and count == 1:
        return

    vector.append(number)

    if number == 1:
        vector.append('|')
        generate(index + 1)

        vector.pop()
        count = 1
        generate(index + 1)
    else:
        if count == 1:
            vector.append('|')
            count = 0
            generate(index + 1)
            vector.pop()

            count = 1
            generate(index + 1)
        else:
            generate(index + 1)

    vector.pop()

if __name__ == "__main__":
    main()
