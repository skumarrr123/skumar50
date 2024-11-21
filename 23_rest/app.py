# MCSK - Suhana Kumar, Margie Cao
# SoftDev k23
# 11/20/24
# time spent: 0.5


from flask import Flask
from flask import render_template
import urllib
import json



T_name = "MCSK"
roster = ["Suhana Kumar, Margie Cao"]


app = Flask(__name__)    #create Flask object


@app.route("/")
def hello():
    file = open("key_nasa.txt","r")
    key = file.readlines()[0]
    uResp = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=' + key)
    info = uResp.read()
    load = json.loads(info)
    print(json.dumps(load))
    return render_template('main.html', T_name=T_name, roster=roster, image1 = load["url"], image2 = load["hdurl"], explanation = load["explanation"])

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()