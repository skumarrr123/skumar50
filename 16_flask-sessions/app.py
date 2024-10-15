'''
Suhana Kumar, Kyle Lee, Vedant Kothari
Team Name: K^3
K16 - Understanding cookies and log in sessions
Time spent: 2
2024-10-11
'''

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'conortoglory'
T_name = "Albania"
roster = ["Suhana Kumar, Vedant Kothari, Kyle Lee"]

@app.route('/')
def primary():
    if 'username' in session:
        return redirect(url_for('submit'))
    return render_template('submit.html',T_name=T_name,roster=roster)

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    session['username'] = username
    return redirect(url_for('welcome'))

@app.route('/welcome')
def welcome():
    if 'username' in session:
        username = session['username']
        greeting = "Hey there "+username+". We hope you like this page"
        method_used = request.method
        explanation = '''
        This is a flask app which checks if you login via a correct username. You will be logged in until you click logout. The app stores sessions via cookies, and the session cookie is sent to your browser.
        '''
        return render_template('response.html', username=username, method=method_used, greeting=greeting, explanation=explanation, T_name=T_name,roster=roster)
    else:
        return redirect(url_for('primary'))

@app.route('/unsubmit')
def unsubmit():
    username = session.pop('username', None)
    return render_template('unsubmit.html', T_name=T_name, roster=roster)

if __name__ == '__main__':
    app.run(debug=True)