price_veggies_kg = float(input())
price_fruit_kg = float(input())
veggies_kg = int(input())
fruit_kg = int(input())

euro = 1.94

total_veggies = price_veggies_kg*veggies_kg
#print(total_veggies)
total_fruit = price_fruit_kg*fruit_kg
#print(total_fruit)

total = (total_fruit+total_veggies) / euro
print(f"{total:.2f}")