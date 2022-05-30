#•	Първи ред – цена на скумрията на килограм. Реално число в интервала [0.00…40.00]
#•	Втори ред – цена на цацата на килограм. Реално число в интервала [0.00…30.00]
#•	Трети ред – килограма паламуд. Реално число в интервала [0.00…50.00]
#•	Четвърти ред – килограма сафрид. Реално число в интервала [0.00… 70.00]
#•	Пети ред – килограма миди. Цяло число в интервала [0 ... 100]
#•	Паламуд – 60% по-скъп от скумрията
#•	Сафрид – 80% по-скъп от цацата
#•	Миди – 7.50 лв. за килограм


price_skumriya = float(input())
price_caca = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

price_palamud = price_skumriya * 1.6
#print(price_palamud)
price_safrid = price_caca * 1.8
#print(price_safrid)
price_midi = 7.50

total = price_palamud*palamud_kg + price_safrid*safrid_kg + price_midi*midi_kg
print(f"{total:.2f}")
