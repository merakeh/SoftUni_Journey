n = int(input())
heroes = {}

for _ in range(n):
    info = input().split(' ')
    hero = info[0]
    hit_points = int(info[1])
    mana_points = int(info[2])

    heroes[hero] = {'hit': hit_points, 'mana': mana_points}

while True:
    data = input().split(' - ')
    if data[0] == "End":
        break

    command = data[0]
    hero_name = data[1]

    if command == "CastSpell":
        mp_needed = int(data[2])
        spell_name = data[3]

        if mp_needed > heroes[hero_name]['mana']:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        else:
            heroes[hero_name]['mana'] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['mana']} MP!")

    elif command == "TakeDamage":
        damage = int(data[2])
        attacker = data[3]
        heroes[hero_name]['hit'] -= damage

        if heroes[hero_name]['hit'] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hit']} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]

    elif command == "Recharge":
        amount = int(data[2])
        initial_mp = heroes[hero_name]['mana']
        heroes[hero_name]['mana'] += amount
        if heroes[hero_name]['mana'] > 200:
            heroes[hero_name]['mana'] = 200
        print(f"{hero_name} recharged for {heroes[hero_name]['mana'] - initial_mp} MP!")

    elif command == "Heal":
        amount = int(data[2])
        initial_hp = heroes[hero_name]['hit']
        heroes[hero_name]['hit'] += amount
        if heroes[hero_name]['hit'] > 100:
            heroes[hero_name]['hit'] = 100
        print(f"{hero_name} healed for {heroes[hero_name]['hit'] - initial_hp} HP!")

for player, points in heroes.items():
    print(player)
    print(f"  HP: {points['hit']}")
    print(f"  MP: {points['mana']}")