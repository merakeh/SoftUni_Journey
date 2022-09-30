
clothes_box = [int(x) for x in input().split()]
rack_capacity = int(input())
capacity = rack_capacity
racks = [1]

while clothes_box:
    top_piece = clothes_box.pop()

    if capacity >= top_piece:
        capacity -= top_piece
    else:
        racks.append(1)
        capacity = rack_capacity
        capacity -= top_piece
print(len(racks))
