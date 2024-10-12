import subprocess

map = {
    "¬": "\\neg ",
    "∨": "\\vee ",
    "∧": "\\land ",
    "→": "\\implies ",
    "∀": "\\forall ",
    "Z": "\\mathbf{Z} ",
    "∈": "\\in ",
    "∃": "\\exists "
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
    buffer = f"${buffer}$"
    print(buffer)
    subprocess.run(['clip.exe'], input=buffer.encode('UTF-16LE'), check=True)