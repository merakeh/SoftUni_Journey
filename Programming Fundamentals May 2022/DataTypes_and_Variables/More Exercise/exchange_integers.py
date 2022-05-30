a = int(input())
b = int(input())

temporary_a = a
temporary_b = b

a = temporary_b
b = temporary_a

print(f"Before:\na = {temporary_a}\nb = {temporary_b}")
print(f"After:\na = {a}\nb = {b}")
