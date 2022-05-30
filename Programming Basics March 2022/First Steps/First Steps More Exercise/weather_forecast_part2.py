temperature = float(input())

if 26 <= temperature <= 35:
    print("Hot")
if 20.1 <= temperature <= 25.9:
    print("Warm")
if 15 <= temperature <= 20:
    print("Mild")
if 12 <= temperature <= 14.9:
    print("Cool")
if 5 <= temperature <= 11.9:
    print("Cold")
if temperature > 35:
    print("unknown")
if temperature < 5:
    print("unknown")
