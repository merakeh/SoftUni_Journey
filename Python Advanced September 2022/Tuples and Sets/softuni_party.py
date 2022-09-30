n = int(input())
guest_list = set()

for o in range(n):
    guest = input()
    guest_list.add(guest)

arriving = input()
while arriving != "END":
    guest_list.remove(arriving)

    arriving = input()

print(len(guest_list))
sorted_list = sorted(guest_list)
print("\n".join(sorted_list))