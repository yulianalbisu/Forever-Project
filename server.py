"""Server for forever app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



@app.route('/') #contains the route I want to form to be
def homepage(): 
    """Sign in before welcome page"""

    return render_template('homepage.html') #contains the form I want to see

@app.route('/new-user')
def create_an_account():
    """Create a new user account"""

    return render_template('create_account.html')

@app.route('/login')
def display_login_form():
    """Display the form for loggin in"""

    return render_template('handle_login.html')

@app.route('/welcome') #changed html for welcome instead of homepage!
def welcome_users():
    """View homepage"""


    return render_template('welcome.html')

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

@app.route('/users')
def all_users():
    """View all users"""

    users = crud.get_users()

    return render_template('all_users.html', users=users)

@app.route('/users/<user_id>')
def show_user(user_id):
    """Show details on a particular user"""

    user = crud.get_user_by_id(user_id) #this may be user_id

    return render_template('user_details.html', user=user)

@app.route('/users', methods=['POST']) #will add to this route the new user
def register_user(): 
    """Create a new user"""


    email = request.form.get('email')
    password= request.form.get('password')
    name = request.form.get('name')

    
    user = crud.get_user_by_email(email) #in crud 
    session['users'] = user

    if user:
        flash('Welcome!')
        return redirect('/login')
        
    else: #this for create account only
        crud.create_user(email, password, name) #from crud
        flash('Account created! Please log in') #when new user directly to get

        return redirect('/login') #it has WELCOME route, but I need it to log in first!! 
                                #redirect if user refuse to sign in

@app.route('/handle_login', methods=['GET', 'POST'])
def login():
    """Existent user can login"""

    email = request.form.get('email')
    password= request.form.get('password')


    user = crud.get_user_by_email(email) #in crud 

    if user:
        if user.password == password:
            flash('Welcome! Get a link')
            return redirect('/link') #change /welcome to link
        else:
            flash('Wrong password')
            return redirect('/') #login form


@app.route('/link')
def create_links():
    """Form to get a link"""

    return render_template('create_link.html')


@app.route('/link', methods=['POST'])
def create_new_link():
    """Create a new link for user"""

    anniversary = request.form.get('anniversary') #if user in users has the same????

     #come from somewhere else

    if user:  #I can see users if i write email
        crud.create_link(anniversary, session['user'].user_id)
        flash('Welcome!')#somehow I DO NOT HOW TO CREATE LINK!
        return render_template('welcome.html')
    if partner not in session:
        flash('Need a Link')
        return redirect('/link') #link form
 



     






if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)