numbers = list(map(int, input().split()))

positive_sum = sum(x for x in numbers if x > 0)
negative_sum = sum(x for x in numbers if x < 0)

print(negative_sum)
print(positive_sum)

if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")