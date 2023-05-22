text = input()
times = input()

try:
    times = int(times)
    repeated_text = text * times
    print(repeated_text)
except ValueError:
    print("Variable times must be an integer")
