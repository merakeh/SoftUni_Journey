employees = list(map(int, input().split()))
factor = int(input())

happiness_each = list(map(lambda x: x * factor, employees))
average_happiness = sum(happiness_each) / len(employees)
overall_happiness = list(filter(lambda x: x >= average_happiness, happiness_each))

if len(overall_happiness) >= len(employees) / 2:
    print(f"Score: {len(overall_happiness)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(overall_happiness)}/{len(employees)}. Employees are not happy!")
