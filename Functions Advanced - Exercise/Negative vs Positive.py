numbers = list(map(int, input().split()))
negatives = [x for x in numbers if x < 0]
positives = [x for x in numbers if x > 0]
print(sum(negatives))
print(sum(positives))
print("The negatives are stronger than the positives" if abs(sum(negatives)) > sum(positives) else "The positives are stronger than the negatives")
