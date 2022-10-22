from collections import deque

mg_caffeine = [int(i) for i in input().split(', ')]
energy_drinks = deque([int(i) for i in input().split(', ')])
max_milligrams = 300
caffeine_intake = 0

while mg_caffeine and energy_drinks:
    last_mg = mg_caffeine.pop()
    first_energy_drink = energy_drinks.popleft()
    result = last_mg * first_energy_drink

    if caffeine_intake + result <= max_milligrams:
        caffeine_intake += result
        continue
    else:
        energy_drinks.append(first_energy_drink)
        caffeine_intake -= 30
        if caffeine_intake < 0:
            caffeine_intake = 0

if energy_drinks:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {caffeine_intake} mg caffeine.")

