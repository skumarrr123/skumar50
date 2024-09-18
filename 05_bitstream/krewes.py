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
devos = []
for tuple in tuples:
    info = tuple.split("$$$")
    if len(info) == 3:
        period, devo, ducky = info
        devos.append({'period': period, 'devo': devo, 'ducky': ducky})
if devos:
    random_devo = random.choice(devos)
    print(f"Devo: {random_devo['devo']}, Period: {random_devo['period']}, Ducky: {random_devo['ducky']}")
else:
        print("No devos found.")