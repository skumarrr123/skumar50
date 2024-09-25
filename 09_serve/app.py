#Kevin Lin, Suhana Kumar, Caden Khuu
#Hello
#SoftDev                                    
#Using flask to print occupation results on webpage
#2024-9-24
#0.5
import csv
import random
from flask import Flask
app = Flask(__name__)

@app.route("/")
def occupation():
    with open('occupations.csv', "r") as file: #Don't have to close
        csvFile = csv.reader(file)
        info = {}
        count = 0
        rando_number = random.randint(0,998)
        total = 0
        for lines in csvFile:
            if not(count == 0): #Removes the first value in the list
                if (total > rando_number):
                    print(lines[0])
                    return(lines[0])
                else:
                    total += (float(lines[1])*10)
                info.update({lines[0]:float(lines[1])})  #Add to dictionary
            count = count + 1
        return ("Hello\n" + info.popitem()) 

def printall():
    with open('occupations.csv', "r") as file: #Don't have to close
        csvFile = csv.reader(file)
        info = """
        <!DOCTYPE html>
        <html>
        <body>
            <p> K^3: Suhana Kumar, Vedant Kothari, Kyle Lee </p>
            
        info += "</body></html>"
        """
        return info



    
if __name__ == '__main__':
    app.run()