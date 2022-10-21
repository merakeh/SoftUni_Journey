
def add_songs(*tuples):
    final_result = ''
    songs = {}
    for el in tuples:
        song, text = el
        if song not in songs:
            songs[song] = []
        songs[song].extend(text)

    for key, value in songs.items():
        final_result += f"- {key}" + '\n'
        if value:
            final_result += '\n'.join(value) + '\n'
    return final_result


print(add_songs(
    ("Love of my life",
    ["Love of my life, you've hurt me",
    "You've broken my heart, and now you leave me",
    "Love of my life, can't you see?",
    "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
    ["Don't take it away from me",
    "Because you don't know",
    "What it means to me"]),
    ("Dream On",
    ["Every time that I look in the mirror"]),
))