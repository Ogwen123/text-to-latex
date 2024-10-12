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

variables = "xXyY"

ASSUME_POWERS = True

while True:
    buffer = ""
    text = input(">")
    pos = 0
    while pos < len(text):
        letter = text[pos]
        if text == "exit": exit()
        if letter in dict.keys(map):
            buffer += map[letter]
        elif letter in variables and ASSUME_POWERS:
            num = ""
            while True:
                if (pos + len(num) + 1) < len(text) and text[pos + len(num) + 1].isnumeric():
                    num += text[pos + len(num) + 1]
                else: break
            buffer += letter if len(num) == 0 else letter + "^" + num
            pos += len(num) + 1
            if not len(num) == 0: print(f"WARNING: assumed that {letter}{num} was meant to be a power and added a ^")
            continue
        else:
            buffer += letter
        pos += 1
        
    buffer = f"${buffer}$"
    print(buffer)
    subprocess.run(['clip.exe'], input=buffer.encode('UTF-16LE'), check=True)