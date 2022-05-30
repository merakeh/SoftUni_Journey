chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
delivery = 2.50

order_chicken = int(input())
order_fish = int(input())
order_vegetarian = int(input())

total = chicken_menu*order_chicken + fish_menu*order_fish + vegetarian_menu*order_vegetarian
#print(total)
dessert = total*0.2
#print(dessert)
final = total + dessert + delivery
print(final)
