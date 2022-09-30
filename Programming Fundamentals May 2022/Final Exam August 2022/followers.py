followers = {}

while True:
    command = input().split(': ')
    if command[0] == "Log out":
        break

    action = command[0]
    username = command[1]

    if action == "New follower":
        if username in followers:
            continue
        else:
            followers[username] = {'likes': 0, 'comments': 0}

    elif action == "Like":
        count = int(command[2])

        if username not in followers:
            followers[username] = {'likes': count, 'comments': 0}
        else:
            followers[username]['likes'] += count

    elif action == "Comment":
        if username not in followers:
            followers[username] = {'likes': 0, 'comments': 1}
        else:
            followers[username]['comments'] += 1

    elif action == "Blocked":
        if username not in followers:
            print(f"{username} doesn't exist.")
        else:
            del followers[username]

print(f"{len(followers)} followers")
for name, info in followers.items():
    total_activity = info['likes'] + info['comments']
    print(f"{name}: {total_activity}")