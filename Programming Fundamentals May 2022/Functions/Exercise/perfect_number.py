
def find_proper_divisor(number):
    divisors = []
    for digit in range(1, number):
        if number % digit == 0:
            divisors.append(digit)
    return divisors


num = int(input())
if sum(find_proper_divisor(num)) == num:
    print("We have a perfect number!")
else:
    print("It\'s not so perfect.")


