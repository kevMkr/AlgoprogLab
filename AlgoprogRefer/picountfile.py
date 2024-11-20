dictt = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0
    }
with open("pi.txt","r") as file:
    ver = file.readlines()
    for i in ver:
        for j in i:
            if j in dictt:
                dictt[j]+=1
print(dictt)