def main():
    songs = list(map(int, input().split(',')))
    start_value = int(input())
    max_val = int(input())
    current_max = start_value

    my_set = set()
    my_list = []

    my_set.add(start_value)
    my_list.append(start_value)

    start_index = 0
    end_index = 0
    last_number_of_tones_added = 0

    for i in range(len(songs)):
        new_tones_added = 0
        for current in range(start_index, end_index + 1):
            new_increment = my_list[current] + songs[i]
            new_decrement = my_list[current] - songs[i]
            if new_increment <= max_val and new_increment not in my_set:
                my_list.append(new_increment)
                my_set.add(new_increment)
                new_tones_added += 1

            if new_decrement >= 0 and new_decrement not in my_set:
                my_list.append(new_decrement)
                my_set.add(new_decrement)
                new_tones_added += 1

        start_index = end_index + 1
        end_index = end_index + new_tones_added
        last_number_of_tones_added = new_tones_added

    for i in range(len(my_list) - last_number_of_tones_added, len(my_list)):
        print(my_list[i])

if __name__ == "__main__":
    main()
