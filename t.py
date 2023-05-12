def fill_the_box(height, length, width, *args):
    volume = height * length * width
    cubes = sum(x for x in args if isinstance(x, (int, float)) and x > 0)
    for el in args:
        if isinstance(el, (int, float)) and el > 0:
            if el > volume:
                difference = el - volume
                volume -= (el - difference)
                cubes -= (el - difference)
            else:
                volume -= el
                cubes -= el
        elif el == 'Finish':
            break
    if volume > 0:
        return f"There is free space in the box. You could put {volume} more cubes."
    else:
        return f"No more free space! You have {cubes} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))