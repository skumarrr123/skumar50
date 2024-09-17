import re
import random
file = open("krewes.txt", "r")
line = file.read()
g = line.split("@@@")
dict1 = {"pd": [], "devo": [], "ducky": []}
for i in range(len(g)):
    lines = g[i]
    f = lines.split("$$$")
    dict1["pd"].append(f[0])
    dict1["devo"].append(f[1])
    dict1["ducky"].append(f[2])
num = random.randint(0,50)

    


print(dict1["pd"][num] + " " + dict1["devo"][num] + " " + dict1["ducky"][num])

    