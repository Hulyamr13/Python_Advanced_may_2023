class Box:
    def __init__(self, width, depth, height):
        self.width = width
        self.depth = depth
        self.height = height


def main():
    boxes_count = int(input())

    boxes = []

    for i in range(boxes_count):
        box_data = list(map(int, input().split()))
        width, depth, height = box_data
        box = Box(width, depth, height)
        boxes.append(box)

    lengths = [1] * boxes_count
    prevs = [-1] * boxes_count

    best_len = 0
    last_index = 0

    for current in range(boxes_count):
        curr_box = boxes[current]

        for prev in range(current - 1, -1, -1):
            prev_box = boxes[prev]

            if (
                prev_box.width < curr_box.width
                and prev_box.depth < curr_box.depth
                and prev_box.height < curr_box.height
                and lengths[prev] + 1 >= lengths[current]
            ):
                lengths[current] = lengths[prev] + 1
                prevs[current] = prev

        if lengths[current] > best_len:
            best_len = lengths[current]
            last_index = current

    stack = []
    while last_index != -1:
        stack.append(boxes[last_index])
        last_index = prevs[last_index]

    for box in reversed(stack):
        print(f"{box.width} {box.depth} {box.height}")


if __name__ == "__main__":
    main()
