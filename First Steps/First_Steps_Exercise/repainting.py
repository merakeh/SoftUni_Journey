nylon = int(input())
paint = int(input())
razreditel = int(input())
workhours = int(input())

sum_nylon = (nylon + 2) * 1.5
sum_paint = paint*1.1 * 14.5
sum_razreditel = razreditel*5
bags = 0.4
materials_total = sum_nylon+sum_paint+sum_razreditel+bags

labour_hour = materials_total*0.3
labour_total = workhours*labour_hour

total = materials_total + labour_total
print(total)
