class Rectangle:
    def __init__(self, name, x1, y1, x2, y2):
        self.Name = name
        self.X1 = x1
        self.Y1 = y1
        self.X2 = x2
        self.Y2 = y2
        self.MaxDepth = 0
        self.BestNested = None

    def __lt__(self, other):
        result = self.MaxDepth - other.MaxDepth
        if result == 0:
            result = -1 if self.Name > other.Name else 1
        return result

    def __str__(self):
        return self.Name

rectangles = []

def main():
    command = input()
    while command != "End":
        tokens = command.split()
        name = tokens[0][0:-1]
        x1, y1, x2, y2 = map(int, tokens[1:])
        rectangle = Rectangle(name, x1, y1, x2, y2)
        rectangles.append(rectangle)
        command = input()

    for rect in rectangles:
        if rect.MaxDepth == 0:
            get_depth(rect)

    max_rect = max(rectangles)
    output = []
    while max_rect:
        output.append(max_rect)
        max_rect = max_rect.BestNested

    print(" < ".join(str(rect) for rect in output))

def get_depth(rect):
    inner_rectangles = []

    for inner_candidate in rectangles:
        if is_inside(inner_candidate, rect) and inner_candidate != rect:
            if inner_candidate.MaxDepth == 0:
                get_depth(inner_candidate)
            inner_rectangles.append(inner_candidate)

    if not inner_rectangles:
        rect.MaxDepth = 1
    else:
        best_nested = max(inner_rectangles)
        rect.BestNested = best_nested
        rect.MaxDepth = best_nested.MaxDepth + 1

def is_inside(inner_rect, rect):
    return (
        inner_rect.X1 >= rect.X1
        and inner_rect.X2 <= rect.X2
        and inner_rect.Y1 <= rect.Y1
        and inner_rect.Y2 >= rect.Y2
    )

if __name__ == "__main__":
    main()
