chrysanthemum_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
is_holiday = input()
chrysanthemum_price = 0
roses_price = 0
tulips_price = 0
bouquet = 0
total_flowers = chrysanthemum_count + roses_count + tulips_count

if season == "Spring" or season == "Summer":
    chrysanthemum_price = chrysanthemum_count * 2
    roses_price = roses_count * 4.1
    tulips_price = tulips_count * 2.5
    bouquet = chrysanthemum_price + roses_price + tulips_price

    if is_holiday == "Y":
        bouquet *= 1.15
    if season == "Spring" and tulips_count > 7:
        bouquet *= 0.95
elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = chrysanthemum_count * 3.75
    roses_price = roses_count * 4.5
    tulips_price = tulips_count * 4.15
    bouquet = chrysanthemum_price + roses_price + tulips_price
    if is_holiday == "Y":
        bouquet *= 1.15
    if season == "Winter" and roses_count >= 10:
        bouquet *= 0.90

if total_flowers > 20:
    bouquet = bouquet * 0.8

final_price = bouquet + 2
print(f"{final_price:.2f}")
