eggs = list(map(int, input().split(", ")))
papers = list(map(int, input().split(", ")))

box = 50
result = 0

while eggs and papers:
    current_egg = eggs[0]
    current_paper = papers[-1]
    if current_egg <= 0:
        eggs.pop(0)
    elif current_egg == 13:
        papers[-1], papers[0] = papers[0], papers[-1]
        eggs.pop(0)
    else:
        if current_egg + current_paper <= box:
            result += 1
            eggs.pop(0)
            papers.pop()
        else:
            eggs.pop(0)
            papers.pop()

if result > 0:
    print(f"Great! You filled {result} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(map(str, eggs))}")
if papers:
    print(f"Pieces of paper left: {', '.join(map(str, papers))}")
