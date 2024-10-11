map = {
    "¬": "\\neg ",
    "∨": "\\vee ",
    "∧": "\\land ",
    "→": "\\implies "
}

while True:
    buffer = ""
    text = input(">")
    for letter in text:
        if text == "exit": exit()
        if letter in dict.keys(map):
            buffer += map[letter]
        else:
            buffer += letter
    print(f"${buffer}$")