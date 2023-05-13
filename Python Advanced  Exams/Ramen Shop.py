bowls_of_ramen = list(map(int, input().split(", ")))
customers = list(map(int, input().split(", ")))

while bowls_of_ramen and customers:
    last_bowl = bowls_of_ramen[-1]
    first_customer = customers[0]
    if first_customer > last_bowl:
        bowls_of_ramen.pop()
        customers[0] -= last_bowl
    elif first_customer < last_bowl:
        customers.pop(0)
        bowls_of_ramen[-1] -= first_customer
    elif first_customer == last_bowl:
        bowls_of_ramen.pop()
        customers.pop(0)

if not customers:
    print("Great job! You served all the customers.")
else:
    print("Out of ramen! You didn't manage to serve all customers.")

if bowls_of_ramen:
    print(f"Bowls of ramen left: {', '.join(map(str, bowls_of_ramen))}")

if customers:
    print(f"Customers left: {', '.join(map(str, customers))}")
