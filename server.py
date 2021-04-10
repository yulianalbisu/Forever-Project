"""Server for forever app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

#comming soon, functions and routes!

@app.route('/')
def homepage():
    """View homepage"""


    return render_template('homepage.html')

@app.route('/questions')
def all_questions():
    """View all questions"""

    questions = crud.get_questions()

    return render_template('all_questions.html', questions=questions)

@app.route('/questions/<question_id>')
def show_question(question_id):
    """Show details of the question"""

    question = crud.get_question_by_id(question_id)

    return render_template('question_details.html', question=question)

@app.route('/register', methods=['POST'])
def register_user():
    email = request.form['email']
    password= request.form['password']

    user = get_user_by_email(email)
    if user:
        return 'This user already exist.'
    else:
        create_user(email, password)

        #return redirect('/login-form')






if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)