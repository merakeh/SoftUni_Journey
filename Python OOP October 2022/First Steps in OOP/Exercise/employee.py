
class Employee:
    def __init__(self, id, first_name, last_name, salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self):
        return self.salary * 12

    def raise_salary(self, amount):
        self.salary += amount
        return self.salary


employee = Employee(744423129, "John", "Smith", 1000)
pers = Employee(595548451, "John", "Cena", 2500)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())

print(pers.get_full_name())

print(pers.raise_salary(5600))

print(pers.get_annual_salary())
