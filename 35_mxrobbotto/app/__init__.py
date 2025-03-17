from flask import Flask, render_template, redirect, url_for, session
from auth import auth_bp
from story import story_bp
from database import init_db, close_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SESSION_PERMANENT'] = False

app.register_blueprint(auth_bp)
app.register_blueprint(story_bp)

db_initialized = False

def clear_session():
    session.clear()

@app.before_request
def initialize_database():
    global db_initialized
    if not db_initialized:
        init_db()
        clear_session()  # Clear session data when the app starts
        db_initialized = True

@app.teardown_appcontext
def teardown_db(exception):
    close_db()

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('story.home'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)