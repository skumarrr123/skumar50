# Suhana Kumar
# K^3 (Suhana Kumar, Vedant Kothari, Kyle Lee)
# SoftDev
# K11 basics of static folder
# <20244><09><26>
# time spent: 0.5


# DEMO
# basics of /static folder
import random
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"


@app.route("/static/foo.html")
def h():
    print("the __name__ of this module is... ")
    print(__name__)
    return str(random.random())

@app.route("/static/fixie.html")
def g():
    print("the __name__ of this module is... ")
    print(__name__)
    return "TNPG: K^3 Names: Vedant Kothari, Suhana Kumar, Kyle Lee"


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()