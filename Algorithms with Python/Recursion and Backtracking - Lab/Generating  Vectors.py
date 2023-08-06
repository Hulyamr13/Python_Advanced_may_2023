def gen01(idx, vector):
    if idx == len(vector):
        print(''.join(str(bit) for bit in vector))
    else:
        for number in range(2):
            vector[idx] = number
            gen01(idx + 1, vector)

n = int(input())
vector = [0] * n
gen01(0, vector)
