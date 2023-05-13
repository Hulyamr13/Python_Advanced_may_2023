def stock_availability(inventory, command, *args):
    if command == "delivery":
        for arg in args:
            inventory.append(arg)
    elif command == "sell":
        if len(args) == 0:
            inventory.pop(0)
        elif isinstance(args[0], int):
            for i in range(args[0]):
                inventory.pop(0)
        elif isinstance(args[0], str):
            flavors_to_remove = [flavor for flavor in args if flavor in inventory]
            for flavor in flavors_to_remove:
                while flavor in inventory:
                    inventory.remove(flavor)
    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
