field_size = int(input())
bomb_number = int(input())
positions_list = []
row_nums = []
col_nums = []

directions_dict = {'up': [-1, 0],
                   'down': [1, 0],
                   'left': [0, -1],
                   'right': [0, 1],
                   'diag_one': [-1, -1],
                   'diag_two': [-1, 1],
                   'diag_tree': [1, -1],
                   'diag_four': [1, 1]}  # row col

for i in range(bomb_number):
    positions = input().split(', ')
    nums = []
    for i in positions:
        num = ''
        for let in i:
            if let.isnumeric():
                num += let
        nums.append(num)
    rr = int(nums[0])
    cc = int(nums[1])
    positions_list.append([rr, cc])

field_with_bombs_only = [[0] * field_size for i in range(field_size)]

while positions_list:
    if positions_list:
        coordinate = positions_list.pop()
        row_bomb = int(coordinate[0])
        col_bomb = int(coordinate[1])
        field_with_bombs_only[row_bomb][col_bomb] = '*'

diag_one = False
diag_two = False
second_digit = field_size - 1

for rows in range(field_size):
    for cols in range(field_size):
        if field_with_bombs_only[rows][cols] == '*':
            for k, v in directions_dict.items():
                change_r = rows + v[0]
                change_c = cols + v[1]
                check_valid_r = 0 <= rows + v[0] < field_size
                check_valid_c = 0 <= cols + v[1] < field_size
                if check_valid_c and check_valid_r:
                    if field_with_bombs_only[change_r][change_c] != '*':
                        field_with_bombs_only[change_r][change_c] += 1

res = ''
for i in field_with_bombs_only:
    res += f"{' '.join([str(b) for b in i])}\n"

print(res)