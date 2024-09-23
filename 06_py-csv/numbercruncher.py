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
def weighted():
    rand = random.uniform(0, float(spamreader[len(spamreader) - 1][1]))    # generates a random num between 0 and the total 99.8
    for i in range(1, len(spamreader) - 1):
        rand -= float(spamreader[i][1])# subtracts random float by the percentage until < 0
        if rand <= 0:
            return f"{columns[0]}:  {occupations_dict[columns[0]][i - 1]}"

print(weighted()) 
   
