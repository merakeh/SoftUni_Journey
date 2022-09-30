resources = {}
current_resource = input()

while current_resource != "stop":
    quantity = int(input())

    if current_resource not in resources.keys():
        resources[current_resource] = 0
    resources[current_resource] += quantity

    current_resource = input()

for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")
