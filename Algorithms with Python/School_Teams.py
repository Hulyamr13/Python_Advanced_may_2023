import itertools

# Read input
girls = input().split(", ")
boys = input().split(", ")

# Generate combinations
girls_combinations = list(itertools.combinations(girls, 3))
boys_combinations = list(itertools.combinations(boys, 2))

# Print combinations
for girls_comb in girls_combinations:
    for boys_comb in boys_combinations:
        print(f"{', '.join(girls_comb)}, {', '.join(boys_comb)}")
