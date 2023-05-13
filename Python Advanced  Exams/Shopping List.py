def shopping_list(budget, **products):
    if budget < 100:
        return "You do not have enough budget."

    basket = []
    total_spent = 0

    for product, (price, quantity) in products.items():
        if len(basket) == 5:
            break

        if price * quantity <= budget - total_spent:
            total_spent += price * quantity
            basket.append((product, price, quantity))

    return '\n'.join([f"You bought {product} for {price*quantity:.2f} leva."
                      for product, price, quantity in basket])


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
