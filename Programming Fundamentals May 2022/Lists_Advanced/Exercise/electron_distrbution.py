number_of_electrons = int(input())

shells = [0] * 10

for shell in range(1, len(shells) + 1):
    max_electrons = 2*(shell**2)
    if max_electrons > number_of_electrons:
        shells[shell] = number_of_electrons
        break
    number_of_electrons -= max_electrons
    shells[shell] += max_electrons

result = list(filter(lambda x: x > 0, shells))
print(result)
