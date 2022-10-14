
def kwargs_length(**d):
    return len(d)


dictionary = {'name': 'Peter', 'age': 25, "person": "Ivan", 'town': "Blalaa"}

print(kwargs_length(**dictionary))