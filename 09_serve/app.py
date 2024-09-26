# Suhana Kumar
# K^3 (Suhana Kumar, Vedant Kothari, Kyle Lee)
# Printing random occupation to web
# .75
# <2024><09><25>
import csv
import random
from flask import Flask
app = Flask(__name__)

@app.route("/")
def occupation():
    with open('occupations.csv', 'r') as csvFile:
        csv_reader = csv.reader(csvFile)
        info = {}
        count = 0
        rando_number = random.randint(0, 998)
        total = 0
        for lines in csv_reader:
            if count == 0:
                count += 1  # Skip the first row with headers
                continue

            if total > rando_number:
                return lines[0]  # Return selected occupation based on random number

            total += float(lines[1]) * 10  # Update cumulative total
            info[lines[0]] = float(lines[1])  # Populate occupation dictionary
            count += 1

        return "Error: Could not select an occupation."  # Default if no occupation found

@app.route("/printall")
def printall():
    with open('occupations.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        occupations = [row for row in reader]

    selected_occupation = random.choice(occupations)

    info = """
    <!DOCTYPE html>
    <html>
    <body>
        <p>K^3: Suhana Kumar, Vedant Kothari, Kyle Lee</p>
        <h2>This time: {}</h2>
        <h3>Occupations</h3>
        <ul>
    """.format(selected_occupation[0])

    for row in occupations:
        info += "<li>{}: {}</li>".format(row[0], row[1])

    info += """
        </ul>
    </body>
    </html>
    """

    return info


if __name__ == '__main__':
    app.run()