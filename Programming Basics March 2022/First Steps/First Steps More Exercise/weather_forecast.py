#При въвеждане на "sunny" трябва да
# се отпечата "It's warm outside!".
# Във всички останали случаи трябва да се отпечата "It's cold outside!".

weather = str(input())
sunny = str("sunny")

if weather == sunny:
    print("It\'s warm outside!")
else:
    print("It\'s cold outside!")
