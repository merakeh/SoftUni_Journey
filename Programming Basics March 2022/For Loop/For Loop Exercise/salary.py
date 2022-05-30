n = int(input())
salary = int(input())
fine_amount = 0

for number in range(1, n + 1):
    website = input()
    if website == "Facebook":
        fine_amount += 150
    elif website == "Instagram":
        fine_amount += 100
    elif website == "Reddit":
        fine_amount += 50

difference = salary - fine_amount

if difference <= 0:
    print("You have lost your salary.")
else:
    print(difference)
