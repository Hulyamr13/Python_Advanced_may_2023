import sys

field_size = int(sys.stdin.readline().strip())
moving_commands = sys.stdin.readline().strip().split(",")
field = []
row_index, column_index = -1, -1

for i in range(field_size):
    row = sys.stdin.readline().strip().split(" ")
    field.append(row)
    for j in range(field_size):
        if row[j] == "D":
            row_index, column_index = i, j

total_money = 0
caught = False

for cmd in moving_commands:
    if cmd == "up":
        if row_index - 1 >= 0:
            field[row_index][column_index] = "+"
            row_index -= 1
        else:
            print("You cannot leave the town, there is police outside!")
    elif cmd == "down":
        if row_index + 1 < field_size:
            field[row_index][column_index] = "+"
            row_index += 1
        else:
            print("You cannot leave the town, there is police outside!")
    elif cmd == "left":
        if column_index - 1 >= 0:
            field[row_index][column_index] = "+"
            column_index -= 1
        else:
            print("You cannot leave the town, there is police outside!")
    elif cmd == "right":
        if column_index + 1 < field_size:
            field[row_index][column_index] = "+"
            column_index += 1
        else:
            print("You cannot leave the town, there is police outside!")

    if field[row_index][column_index] == "P":
        print(f"You got caught with {total_money}$, and you are going to jail.")
        field[row_index][column_index] = "#"
        caught = True
        break
    elif field[row_index][column_index] == "$":
        money = row_index * column_index
        print(f"You successfully stole {money}$.")
        total_money += money

    field[row_index][column_index] = "D"

if not caught:
    print(f"Your last theft has finished successfully with {total_money}$ in your pocket.")

for row in field:
    print(" ".join(row))
