# Suhana Kumar
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)          # should work and create a page with 'No hablo queso!'

@app.route("/")                # prediction was accurate
def hello_world():
    print(__name__)            # 
    return "No hablo queso!"   # ...

app.run()                      # ...
                