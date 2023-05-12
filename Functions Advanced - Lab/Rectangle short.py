def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"
    area = lambda l, w: l * w
    perimeter = lambda l, w: 2 * (l + w)
    return f"Rectangle area: {area(length, width)}\nRectangle perimeter: {perimeter(length, width)}"


print(rectangle(2, 10))
print(rectangle('2', 10))