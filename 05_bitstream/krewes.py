# Suhana Kumar
# K^3 (Suhana Kumar, Vedant Kothari, Kyle Lee)
# SoftDev
# Learn more about reading a file and using the random function on it
# 2024-09-17
# .75

import random
with open("krewes.txt", "r") as file:
    f = file.read()
tuples = f.split("@@@")
#splits by devo
devos = []
for tuple in tuples: #iterates through each tuple
    info = tuple.split("$$$")
#splits each devo's information into thier period, name and duck name
    if len(info) == 3:
        period, devo, ducky = info
        devos.append({'period': period, 'devo': devo, 'ducky': ducky})#adds the info for each devo into a list as its own index
if devos:
    random_devo = random.choice(devos)#chosses random devo
    print(f"Devo: {random_devo['devo']}, Period: {random_devo['period']}, Ducky: {random_devo['ducky']}")
else:
        print("No devos found.")
        
