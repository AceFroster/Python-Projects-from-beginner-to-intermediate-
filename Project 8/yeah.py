file = "true"
file2 = "love"

def calculate_love_score(firstname, secondname):
    fullname = (firstname + secondname).lower()
    okay = 0
    olo = 0
    for i in fullname:
        if i in file:
            okay += 1
        if i in file2:
            olo += 1

    score = int(str(okay) + str(olo))
    print(score)


calculate_love_score("rutu", "lomo")



