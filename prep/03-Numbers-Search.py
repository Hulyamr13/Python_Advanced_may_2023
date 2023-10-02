import collections


def numbers_searching(*args):
    no_dupll = set(args)
    numbers = []

    for el in args:
        numbers.append(el)


    duplicates = [item for item, count in collections.Counter(numbers).items() if count > 1]
  #  duplicates = sorted([item for item, count in collections.Counter(numbers).items() if count > 1])
    duplicates.sort()


    missing = [el for el in range(min(no_dupll), max(no_dupll)+1) if el not in no_dupll][0]   # za judge trqbva da izpozvame set() --> no_dubll
   # missing = [el for el in range(min(duplicates), max(duplicates)+1) if el not in duplicates][0]


    return [missing, duplicates]



print(numbers_searching(1, 2, 4, 2, 5, 4))

print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))