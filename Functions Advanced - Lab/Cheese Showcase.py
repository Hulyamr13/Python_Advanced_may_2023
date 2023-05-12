def sorting_cheeses(**cheeses):
    sorted_cheeses = sorted(cheeses.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""
    for cheese, quantities in sorted_cheeses:
        result += f"{cheese}\n"
        quantities.sort(reverse=True)
        result += "\n".join(str(qty) for qty in quantities) + "\n"

    return result.strip()


print(sorting_cheeses(Parmesan=[102, 120, 135], Camembert=[100, 100, 105, 500, 430], Mozzarella=[50, 125]))
print(sorting_cheeses(Parmigiano=[165, 215], Feta=[150, 515], Brie=[150, 125]))