def find_strongest_eggs(elements: list, sub_list):
    sub_listed_elements = [[] for x in range(sub_list)]
    ind = 0

    while elements:
        if ind == sub_list:
            ind = 0

        element = elements.pop(0)
        sub_listed_elements[ind].append(element)
        ind += 1

    valid = []
    for sub_listed_el in sub_listed_elements:
        pairs = len(sub_listed_el) // 2

        # mid_egg = sub_listed_el[pairs]
        # left_egg = sub_listed_el[pairs - 1]
        # right_egg = sub_listed_el[pairs + 1]
        # condition1 = left_egg < mid_egg > right_egg
        # condition2 = right_egg > left_egg
        #
        # if condition1 and condition2:
        #     valid.append(mid_egg)

        is_valid = True
        middle_position_egg = sub_listed_el[pairs]
        if middle_position_egg > sub_listed_el[pairs + 1] > sub_listed_el[pairs - 1]:
            for i in range(pairs):
                first_el = sub_listed_el[i]
                second_el = sub_listed_el[-(i + 1)]

                if first_el > second_el:
                    is_valid = False
                    break
            if is_valid:
                valid.append(middle_position_egg)

    return valid


test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))

test = ([-1, 0, 2, 5, 2, 3], 2)
print(find_strongest_eggs(*test))

test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))

test = ([1, 10, 2], 1)
print(find_strongest_eggs(*test))