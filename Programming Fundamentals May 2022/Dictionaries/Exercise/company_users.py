
companies = {}
command = input()

while command != "End":
    company_name, employee_id = command.split(' -> ')
    if company_name not in companies:
        companies[company_name] = []
    if employee_id in companies.values():
        command = input()
        continue
    companies[company_name].append(employee_id)

    command = input()

for company, ids in companies.items():
    print(company)
    for name in ids:

        print(f"-- {name}")
