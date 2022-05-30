num = int(input())
sum_of_ascii = 0

for i in range(num):
    symbol = input()
    sum_of_ascii += ord(symbol)

print(f"The sum equals: {sum_of_ascii}")
