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
    """Show homepage with options to login and create an account"""


    return render_template('homepage.html') #contains the form I want to see

@app.route('/new-user')
def create_an_account():
    """Displays a form to create a new user"""

    return render_template('create_account.html')

@app.route('/login')
def display_login_form():
    """Display the form for loggin in"""

    return render_template('handle_login.html')

@app.route('/welcome') #changed html for welcome instead of homepage!
def welcome_users():
    """After login options to see another user, with same link key"""


    return render_template('welcome.html')


@app.route('/users')
def all_users():
    """View all users"""

    users = crud.get_users()

    return render_template('all_users.html', users=users)

@app.route('/users/<user_id>')
def show_user(user_id):
    """Show details on a particular user"""
    # check if user_id passed in is user_id in session
    if 'user_id' in session:
        user = crud.get_user_by_id(user_id) #this may be user_id
        link = crud.get_link_id(user_id)
        return render_template('user_details.html', user=user, link=link)
    else:
        flash('Something went wrong')
        return redirect('/')


@app.route('/users', methods=['POST']) #will add to this route the new user
def register_user(): 
    """Create a new user and link"""

    email = request.form.get('email')
    password= request.form.get('password')
    name = request.form.get('name')
    anniversary = request.form.get('anniversary')

    user = crud.get_user_by_email(email) #in crud 
    
    if user:
        flash('Welcome!')
        # need to check if user is in session first, if not, redirect to /login
        return redirect(f'/users/{user.user_id}')
        
    else: #this for create account only
        new_user = crud.create_user(email, password, name)
        new_link = crud.create_link(anniversary, new_user.user_id) #from crud
        flash('Account created! Please log in') #when new user directly to get

        return redirect('/login') #it has WELCOME route, but I need it to log in first!! 
                                #redirect if user refuse to sign in

@app.route('/handle_login', methods=['POST'])
def login():
    """Existent user can login"""
 
    email = request.form.get('email')
    password= request.form.get('password')

    user = crud.get_user_by_email(email) #in crud 

    if user and user.password == password:
        session['user_id'] = user.user_id
        flash('Welcome! Get a link')
        return redirect(f'/users/{user.user_id}') 
    else:
        flash('Wrong password')
        return redirect('/login') #login form



#CREATE LINK, RETURN LINK TO USER, PLACE LINK TO VALIDATE

@app.route('/handle_links')
def handle_links():
    """User will get a link, to connect partner"""




@app.route('/links')
def get_links():
    """Verifiying if user has link, redirect '/welcome'"""


    link = crud.get_link_by_id(link_id)

    return render_template('create_link.html', link_id=link_id)



@app.route('/links/<link_id>')
def show_link(link_id):
    """Show details on a particular user"""

    link = crud.get_link_by_id(link_id) #this may be user_id

    return render_template('link_details.html', link=link)
 
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


     






if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)