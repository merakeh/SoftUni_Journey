x = float(input())    #Visochina na kushtata
y = float(input())   #Duljina na stranichnata stena
h = float(input())   #Visochina na triugulnata strana na pokriva

front_area = x*x-1.2*2
#print(front_area)
back_area = x*x
#print(back_area)
side_area = x*y - 1.5*1.5
#print(side_area)

green_area = front_area + back_area + 2*side_area
#print(green_area)
green_paint = green_area/3.4
print(f"{green_paint:.2f}")

roof_rectangle_area = x*y*2
roof_triangle_area = (x*h/2) * 2
red_area = roof_triangle_area + roof_rectangle_area
#print(red_area)
red_paint = red_area/4.3
print(f"{red_paint:.2f}")