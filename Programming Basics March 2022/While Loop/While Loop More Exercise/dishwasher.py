detergent_bottles = int(input())
total_detergent_ml = detergent_bottles * 750
counter_rounds = 0
dishes = 0
pots = 0
is_enough = True

input_line = input()
while input_line != "End":
    count_plates = int(input_line)
    counter_rounds += 1
    if counter_rounds % 3 == 0:
        total_detergent_ml -= count_plates * 15
        pots += count_plates
    else:
        total_detergent_ml -= count_plates * 5
        dishes += count_plates

    if total_detergent_ml <= 0:
        is_enough = False
        break

    input_line = input()

if not is_enough:
    print(f"Not enough detergent, {abs(total_detergent_ml)} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {total_detergent_ml} ml.")
