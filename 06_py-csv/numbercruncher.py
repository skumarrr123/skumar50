# Suhana Kumar
# K^2 (Suhana Kumar, Vedant Kothari)
# SoftDev
# Learn more about reading a CSV file specifically and using the random function on it
# <2024>-<09>-<19>
# time spent: 0.75 hours

import csv, random
with open('occupations.csv', newline='') as csvfile: # opens the csv file
    spamreader = list(csv.reader(csvfile)) # used by others
    columns = spamreader[0] # creates 'columns' for job class and percentage
    occupations_dict = {columns[0] : [], columns[1] : []} # job class has its own values and percentages has its own values
    for i in range(1,len(spamreader) - 1): # ensures that columns with total and job class title are not included
        occupations_dict[columns[0]].append(spamreader[i][0]) # adds all job classes as values to job class key
        occupations_dict[columns[1]].append(float(spamreader[i][1])) # converts percentages to numbers and adds them as values to percentage key
    num = random.randint(1, 998) # multiplied all percentages by 100 to make numbers more convenient
    if (num >= 1 and num <= 61): # sort through every scenario, despite not being the most efficient method
        print(occupations_dict[columns[0]][0])
    if (num >= 62 and num <= 111):
        print(occupations_dict[columns[0]][1])
    if (num >= 112 and num <= 138):
        print(occupations_dict[columns[0]][2])
    if (num >= 139 and num <= 155):
        print(occupations_dict[columns[0]][3])
    if (num >= 156 and num <= 164):
        print(occupations_dict[columns[0]][4])
    if (num >= 165 and num <= 180):
        print(occupations_dict[columns[0]][5])
    if (num >= 181 and num <= 188):
        print(occupations_dict[columns[0]][6])
    if (num >= 189 and num <= 249):
        print(occupations_dict[columns[0]][7])
    if (num >= 250 and num <= 266):
        print(occupations_dict[columns[0]][8])
    if (num >= 267 and num <= 321):
        print(occupations_dict[columns[0]][9])
    if (num >= 322 and num <= 349):
        print(occupations_dict[columns[0]][10])
    if (num >= 350 and num <= 372):
        print(occupations_dict[columns[0]][11])
    if (num >= 373 and num <= 455):
        print(occupations_dict[columns[0]][12])
    if (num >= 456 and num <= 492):
        print(occupations_dict[columns[0]][13])
    if (num >= 493 and num <= 532):
        print(occupations_dict[columns[0]][14])
    if (num >= 533 and num <= 634):
        print(occupations_dict[columns[0]][15])
    if (num >= 635 and num <= 785):
        print(occupations_dict[columns[0]][16])
    if (num >= 786 and num <= 791):
        print(occupations_dict[columns[0]][17])
    if (num >= 792 and num <= 834):
        print(occupations_dict[columns[0]][18])
    if (num >= 835 and num <= 872):
        print(occupations_dict[columns[0]][19])
    if (num >= 873 and num <= 933):
        print(occupations_dict[columns[0]][20])
    if (num >= 934 and num <= 998):
        print(occupations_dict[columns[0]][21])