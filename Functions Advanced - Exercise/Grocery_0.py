def grocery_store(**items):
    sorted_items = sorted(items.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = ""
    for item in sorted_items:
        result += f"{item[0]}: {item[1]}\n"
    return result.strip()


print(grocery_store(
 bread=5,
 pasta=12,
 eggs=12,
))
print(grocery_store(
 bread=2,
 pasta=2,
 eggs=20,
 carrot=1,
))