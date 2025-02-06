import subprocess

map = {
    "¬": "\\neg ",
    "∨": "\\vee ",
    "∧": "\\land ",
    "→": "\\implies ",
    "∀": "\\forall ",
    "∈": "\\in ",
    "∃": "\\exists ",
    "≡": "\\equiv "
}

variables = "xXyY"

ESCAPE_SPACES = FALSE
ASSUME_POWERS = True
ADD_DOLLAR_SIGNS = False
REPLACE_Z_WITH_INTEGER_SYMBOL = False

if REPLACE_Z_WITH_INTEGER_SYMBOL: map["Z"] = "\\mathbf{Z} "

while True:
    buffer = ""
    text = input(">")
    if text == "ES":
        ESCAPE_SPACES = not ESCAPE_SPACES
        continue
    elif text == "AP":
        ASSUME_POWERS = not ASSUME_POWERS
        continue
    elif text == "DS":
        ADD_DOLLAR_SIGNS = not ADD_DOLLAR_SIGNS
        continue
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
        elif ESCAPE_SPACES and letter == " ":
            buffer += "\ "
        else:
            buffer += letter
        pos += 1
        
    buffer = f"${buffer}$" if ADD_DOLLAR_SIGNS else buffer
    print(buffer)
    subprocess.run(['clip.exe'], input=buffer.encode('UTF-16LE'), check=True)