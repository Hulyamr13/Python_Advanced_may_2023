def shop_from_grocery_list(budget, grocery_list, *products):
    purchased = []
    missing = []
    total_price = 0
    for product, price in products:
        if product not in grocery_list:
            continue
        if price > budget - total_price:
            break
        if product in purchased:
            continue
        purchased.append(product)
        total_price += price
    budget_left = budget - total_price
    if len(purchased) == len(grocery_list):
        return f"Shopping is successful. Remaining budget: {budget_left:.2f}."
    else:
        for product in grocery_list:
            if product not in purchased:
                missing.append(product)
        return f"You did not buy all the products. Missing products: {', '.join(missing)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
