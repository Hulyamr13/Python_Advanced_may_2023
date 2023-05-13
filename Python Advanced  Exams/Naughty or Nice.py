def naughty_or_nice_list(santa_list, *args, **kwargs):
    nice_list = []
    naughty_list = []
    not_found_list = []

    # Process args commands
    for arg in args:
        count, state = arg.split("-")
        count = int(count)
        candidates = [kid for kid in santa_list if kid[0] == count]
        if len(candidates) == 1:
            kid = candidates[0]
            santa_list.remove(kid)
            if state == "Nice":
                nice_list.append(kid[1])
            elif state == "Naughty":
                naughty_list.append(kid[1])

    # Process kwargs commands
    for name, state in kwargs.items():
        candidates = [kid for kid in santa_list if kid[1] == name]
        if len(candidates) == 1:
            kid = candidates[0]
            santa_list.remove(kid)
            if state == "Nice":
                nice_list.append(kid[1])
            elif state == "Naughty":
                naughty_list.append(kid[1])

    # Process remaining kids
    for kid in santa_list:
        not_found_list.append(kid[1])

    # Format and return results
    results = []
    if nice_list:
        results.append("Nice: " + ", ".join(nice_list))
    if naughty_list:
        results.append("Naughty: " + ", ".join(naughty_list))
    if not_found_list:
        results.append("Not found: " + ", ".join(not_found_list))
    return "\n".join(results)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
