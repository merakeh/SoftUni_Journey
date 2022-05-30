print("What amount do you deposit?")
deposit = float(input())
print("How many months do you want to calculate?")
months = int(input())
print("what is the yearly percent?")
yearly_percent = float(input()) / 100

sum = deposit + months * ((deposit*yearly_percent) / 12)
print(sum)
