width = float(input()) * 100
height = float(input()) * 100
3 <= height <= width <= 100

workplace_height = 70
workplace_width = 120
hallway = 100

# Obshtiya broi se presmyata broy po shirochina*broy po duljina - 3 broya ot vratata i katedrata
height_count = (height - hallway) //workplace_height
#print(height_count)
width_count = width // workplace_width
#print(width_count)
total_workplaces = height_count*width_count -3
print(total_workplaces)