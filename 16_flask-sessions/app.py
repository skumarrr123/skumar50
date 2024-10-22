
""" simple all-in-one flask app with session handling
"""

'''
 Suhana Kumar, Kyle Lee, Vedant Kothari,
Team Name: K^3
K16 - Take and Keep
2024-10-14
'''

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'conortoglory'
T_name = "K^3"
roster = ["Kyle Lee, Vedant Kothari, Suhana Kumar"]

@app.route('/')
def primary():
    if 'username' in session: #Checks if there is an active session currently
        return redirect(url_for('submit'))
    return render_template('submit.html',T_name=T_name,roster=roster) #Renders submit.html on the page if there is no active session

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    session['username'] = username #Stores username in a session
    return redirect(url_for('welcome'))

@app.route('/welcome')
def welcome():
    if 'username' in session:
        username = session['username']
        greeting = "Hey there "+username+". We hope you like this page" #Returns greeting once user submits username or is already logged in
        method_used = request.method
        explanation = '''
        This is a flask app which checks if you login via a correct username. You will be logged in until you click logout. The app stores sessions via cookies, and the session cookie is sent to your browser.
        '''
        return render_template('response.html', username=username, method=method_used, greeting=greeting, explanation=explanation, T_name=T_name,roster=roster)
    else:
        return redirect(url_for('primary'))

@app.route('/unsubmit')
def unsubmit():
    username = session.pop('username', None) #Removes user from session
    return render_template('unsubmit.html', T_name=T_name, roster=roster)

if __name__ == '__main__':
    app.run(debug=True)
