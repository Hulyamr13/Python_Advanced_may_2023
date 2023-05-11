input_str = input()

num_lists = [list(map(int, lst.split())) for lst in input_str.split('|') if lst]

flat_list = [num for sublist in reversed(num_lists) for num in sublist]

print(*flat_list)