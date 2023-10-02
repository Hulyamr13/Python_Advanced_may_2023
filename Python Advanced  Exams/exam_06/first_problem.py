from collections import deque

def resolve_challenges(tools, substances, challenges):
    while challenges:
        tool = tools.popleft()
        substance = substances[-1]
        result = tool * substance

        if result in challenges:
            challenges.remove(result)
            substances.pop()
        else:
            tools.append(tool + 1)
            substances[-1] -= 1
            if substances[-1] == 0:
                substances.pop()

        if not substances:
            return False

    return True

def main():
    tools = deque(map(int, input().split()))
    substances = list(map(int, input().split()))
    challenges = list(map(int, input().split()))

    if resolve_challenges(tools, substances, challenges):
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
    else:
        print("Harry is lost in the temple. Oblivion awaits him.")

    if tools:
        print("Tools:", ', '.join(map(str, list(tools))))
    if substances:
        print("Substances:", ', '.join(map(str, substances)))
    if challenges:
        print("Challenges:", ', '.join(map(str, challenges)))

if __name__ == '__main__':
    main()
