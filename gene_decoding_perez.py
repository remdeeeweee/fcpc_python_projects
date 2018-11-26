
name_1 = input("Please enter your name:") #ABC-DEF-GHI-JKL-MNO-PQR-STU-VWX-ZZZ

user_2 = ""

for x in range(len(name_1)):
    char = name_1[x]


    if char == "A":
        user_2 += "B"
    elif char == "B":
        user_2 += "C"
    elif char == "C":
        user_2 += "D"
    elif char == "D":
        user_2 += "E"
    elif char == "E":
        user_2 += "F"
    elif char == "F":
        user_2 += "G"
    elif char == "G":
        user_2 += "H"
    elif char == "H":
        user_2 += "I"
    elif char == "I":
        user_2 += "J"
    elif char == "J":
        user_2 += "K"
    elif char == "K":
        user_2 += "L"
    elif char == "L":
        user_2 += "M"
    elif char == "M":
        user_2 += "N"
    elif char == "N":
        user_2 += "O"
    elif char == "O":
        user_2 += "P"
    elif char == "P":
        user_2 += "Q"
    elif char == "Q":
        user_2 += "R"
    elif char == "R":
        user_2 += "S"
    elif char == "S":
        user_2 += "T"
    elif char == "T":
        user_2 += "U"
    elif char == "U":
        user_2 += "V"
    elif char == "V":
        user_2 += "W"
    elif char == "W":
        user_2 += "X"
    elif char == "X":
        user_2 += "Y"
    elif char == "Y":
        user_2 += "Z"
    elif char == "Z":
        user_2 += "A"
    else:
        user_2 += char

print(user_2)
