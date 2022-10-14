
def sum_nums(seq):
    positive = 0
    negative = 0
    for num in seq:
        if num > 0:
            positive += num
        else:
            negative += num

    return positive, negative


sequence = [int(x) for x in input().split()]

print(sum_nums(sequence)[1])   # negative
print(sum_nums(sequence)[0])   # positive

if abs(sum_nums(sequence)[1]) == sum_nums(sequence)[0]:
    print("They are equal!")
elif abs(sum_nums(sequence)[1]) > sum_nums(sequence)[0]:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")