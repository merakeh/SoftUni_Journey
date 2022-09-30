
first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(x) for x in input().split()])

n = int(input())

for _ in range(n):
    line = input().split(maxsplit=2)
    command = line[0] + line[1]

    if "AddFirst" == command:
        numbers = [int(x) for x in line[2].split()]
        for num in numbers:
            first_sequence.add(num)
    elif "AddSecond" == command:
        numbers = [int(x) for x in line[2].split()]
        for num in numbers:
            second_sequence.add(num)

    elif "RemoveFirst" == command:
        numbers = [int(x) for x in line[2].split()]
        for num in numbers:
            first_sequence.discard(num)
    elif "RemoveSecond" == command:
        numbers = [int(x) for x in line[2].split()]
        for num in numbers:
            second_sequence.discard(num)
    elif "CheckSubset" == command:
        print(second_sequence.issubset(first_sequence))
first_sorted = sorted(first_sequence)
second_sorted = sorted(second_sequence)

print(', '.join([str(n) for n in first_sorted]))
print(', '.join([str(n) for n in second_sorted]))
