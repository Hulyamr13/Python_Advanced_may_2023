def age_assignment(*names, **ages):
    result = []
    for name in names:
        age_key = name[0]
        age = ages[age_key]
        result.append(f"{name} is {age} years old.")
    return "\n".join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36,
A=22, B=61))