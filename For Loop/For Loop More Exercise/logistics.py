number_of_cargos = int(input())
sum_cargo_t = 0
bus_tons = 0
truck_tons = 0
train_tons = 0


for shipping in range(1, number_of_cargos+1):
    tons_of_cargo = int(input())
    sum_cargo_t += tons_of_cargo

    if tons_of_cargo <= 3:
        bus_tons += tons_of_cargo
    elif 4 <= tons_of_cargo <= 11:
        truck_tons += tons_of_cargo
    else:
        train_tons += tons_of_cargo

average_sum = (bus_tons * 200 + truck_tons * 175 + train_tons * 120) / sum_cargo_t

percent_bus = bus_tons / sum_cargo_t * 100
percent_truck = truck_tons / sum_cargo_t * 100
percent_train = train_tons / sum_cargo_t * 100

print(f"{average_sum:.2f}")
print(f"{percent_bus:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")
