def list_manipulator(lst, action, position, *args):
    if action == "add":
        if position == "beginning":
            lst = list(args) + lst
        elif position == "end":
            lst += list(args)
    elif action == "remove":
        if position == "beginning":
            if args:
                lst = lst[args[0]:]
            else:
                lst = lst[1:]
        elif position == "end":
            if args:
                lst = lst[:-args[0]]
            else:
                lst = lst[:-1]
    return lst


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
