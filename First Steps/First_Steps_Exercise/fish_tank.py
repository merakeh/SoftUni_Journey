length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent = float(input()) /100

volume = length_cm * width_cm * height_cm
#print(f"The volume of the fish tank is {volume}cm3.")
volume_litres = volume*0.001
#print(f"The volume of the fish tank is {volume}l.")

capacity = volume_litres * (1 - percent)
print(capacity)
