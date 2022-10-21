from collections import deque

eggs = deque([int(x) for x in input().split(', ')])
paper = [int(x) for x in input().split(', ')]
total_boxes = 0

while eggs and paper:
    first_egg = eggs.popleft()

    if first_egg <= 0:
        continue

    if first_egg == 13:
        paper[0], paper[-1] = paper[-1], paper[0]
        continue

    last_paper = paper.pop()

    if first_egg + last_paper <= 50:
        total_boxes += 1

if total_boxes == 0:
    print("Sorry! You couldn't fill any boxes!")
else:
    print(f"Great! You filled {total_boxes} boxes.")

if eggs:
    print(f"Eggs left: {', '.join([str(x) for x in eggs])}")
if paper:
    print(f"Pieces of paper left: {', '.join([str(x) for x in paper])}")
