rooms = int(input())
total_chairs = 0
total_visitors = 0
for room in range(1, rooms + 1):
    info = input().split(' ')
    chairs = info[0]
    visitors = int(info[1])
    total_chairs += len(chairs)
    total_visitors += visitors

    if len(chairs) < visitors:
        print(f"{visitors - len(chairs)} more chairs needed in room {room}")
else:
    total_free_chairs = total_chairs - total_visitors
    if total_free_chairs > 0:
        print(f"Game On, {total_free_chairs} free chairs left")

