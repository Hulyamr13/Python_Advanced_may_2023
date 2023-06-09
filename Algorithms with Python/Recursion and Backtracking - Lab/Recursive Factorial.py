def calc_fact(n):
    if n == 0:
        return 1
    return n * calc_fact(n - 1)

def main():
    n = int(input())
    result = calc_fact(n)
    print(result)

if __name__ == "__main__":
    main()
