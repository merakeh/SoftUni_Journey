number = int(input())
output = ""

if number < 100 and number != 0:
    output = "invalid"
elif number > 200:
    output = "invalid"
print(output)

#  Possible code
valid = (number >= 100 and number <= 200) or number == 0
if not valid:
    print("invalid")
