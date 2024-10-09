'''
Suhana Kumar, Endrit Idrizi, Vedant Kothari
Team Name: Albania
K15 - Echoing responses
Time spent: 0.75
2024-10-08
'''
from flask import Flask, render_template, request

app = Flask(__name__)

T_name = "Albania"
roster = ["Endrit Idrizi, Vedant Kothari, Suhana Kumar"]

@app.route('/')
def primary():
    return render_template('primary.html',T_name=T_name,roster=roster)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    username = request.args.get('username') if request.method == 'GET' else request.form.get('username')
    method_used = request.method
    greeting = "Hey there "+username+". We hope you like this page"
    explanation = '''
    GET sends data via the URL, making it more useful for taking information.
    POST sends data through the body which makes it more useful for modifying data on the server side.
    '''
    return render_template('secondary.html', username=username, method=method_used, greeting=greeting, explanation=explanation, T_name=T_name,roster=roster)

if __name__ == '__main__':
    app.run(debug=True)