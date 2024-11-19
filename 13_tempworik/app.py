
# Jonathan Metzler-Kyle Lee-Suhana Kumar - MLK
# SoftDev
# Sep 2024

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import csv, random
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = []

@app.route("/wdywtbwygp") 
def test_tmplt():
    #starts the table
    page="<table><thead><tr><th>Occupations</th><th>Percentages</th></tr></thead><tbody>"
    with open("occupations.csv", "r") as file:
        next(file)
        f = csv.reader(file)
        dic = {}
        for i in f:
            dic.update({i[0]: float(i[1])})
        total = dic["Total"]
        key = dic.keys()
        for k in key:
            num = dic[k]
            if (num / total) > random.random(): #random.random generates a float in (0, 1)
                thing = k
            else:
                total -= num #Used for weighted probability; subtracts the probability from the total if the occupation is not chosen
    for stuff in dic.keys():
        page = page + stuff + "<br>"
    page += "</tbody></table>"
    return render_template('tablified.html', foo="fooooo", oogada= "combining elements of flask and html", boogada="Jonathan Metzler-Kyle Lee-Suhana Kumar - MLK", collection=coll)


if __name__ == "__main__":
    app.debug = True
    app.run()
