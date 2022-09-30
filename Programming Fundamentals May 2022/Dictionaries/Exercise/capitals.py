countries = input().split(', ')
capitals = input().split(', ')

new_dict = {country: city for country, city in zip(countries, capitals)}
for key, value in new_dict.items():
    print(f"{key} -> {value}")
