'''
Suhana Kumar, Kyle Lee, Vedant Kothari
Team Name: K^3
K16 - Understanding cookies and log in sessions
Time spent: 2
2024-10-11
'''
from flask import Flask, render_template, request

app = Flask(__name__)

T_name = "K^3"
roster = ["Suhana Kumar, Kyle Lee, Vedant Kothari"]

@app.route('/')
def primary():
    return render_template('primary.html',T_name=T_name,roster=roster)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST'
        username = request.form('username')
    if request.method == 'GET'
        username = request.args.get('username')
        
    method_used = request.method
    greeting = "Hey there "+username+". We hope you like this page"
    explanation = '''
    GET sends data via the URL, making it more useful for taking information.
    POST sends data through the body which makes it more useful for modifying data on the server side.
    '''
    return render_template('secondary.html', username=username, method=method_used, greeting=greeting, explanation=explanation, T_name=T_name,roster=roster)

if __name__ == '__main__':
    app.run(debug=True)