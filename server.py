"""Server for forever app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
import crud
from jinja2 import StrictUndefined
import model
from datetime import datetime, date

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



@app.route('/') #contains the route I want to form to be
def homepage(): 
    """Show homepage with options to login and create an account"""


    return render_template('homepage.html') #contains the form I want to see /homepage.html

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


@app.route('/users/<user_id>')
def show_user(user_id):
    """Show details on a particular user"""
    # check if user_id passed in is user_id in session
    if 'user_id' in session:
        user = crud.get_user_by_id(user_id) #this may be user_id
        links = crud.get_links()
        #print(links)
        #print(user_id)

        for id, partner1, partner2 in links:
            if partner1 == user.user_id or partner2 == user.user_id:
                link = model.db.session.query(model.Link).get(id)
                return render_template('user_details.html', user=user, link=link)
            else:
                flash('No links found for you..')
                print('ESTOY AQUI Y NO PASE IF STATEMENT 1!!!!!!')
                return redirect('/connecting')
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

        return redirect('/login') #/loginit has WELCOME route, but I need it to log in first!! 
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


@app.route('/connecting')
def connecting_partner():


    return render_template('connecting_form.html')

@app.route('/connecting', methods=['POST'])
def register_partner():
    """Create partner from user_id1"""

    email = request.form.get('email')
    password= request.form.get('password')
    name = request.form.get('name')
    link_id = request.form.get('link_id')
    link_id = int(link_id)
    anniversary = request.form.get('anniversary')
    anniversary = datetime.strptime(anniversary, '%Y-%m-%d').strftime("%Y-%m-%d")
  
    user = crud.get_user_by_email(email) #in crud 

    if user:
        flash('Welcome!')
        # need to check if user is in session first, if not, redirect to /login
        return redirect(f'/users/{user.user_id}')
        
    else: #this for create account only
        new_user = crud.create_user(email, password, name)
        flash('Account created! Please log in') #when new user directly to get

        link = crud.get_link_by_link_id(link_id)
     
        if link: 
            if anniversary == link.anniversary.strftime("%Y-%m-%d"):
                updated_link = model.Link.query.filter_by(link_id=link_id).update({'partner': new_user.user_id})
                model.db.session.commit()
                return redirect('/login')
            else:
                flash('Remember your anniversary...')
                return redirect('/connecting')
        else:
            flash('Cannot find your partner')
            return redirect('/connecting')


@app.route('/questions')
def all_questions():
    """View all questions"""
    if 'user_id' in session:
        user = crud.get_user_by_id(session['user_id'])
        questions = crud.get_questions()
        # question = crud.get_question_by_id(question_id)
        return render_template('all_questions.html', questions=questions)

    else:
        return redirect('/login')   

@app.route('/handle_answers', methods=['POST'])
def register_answers():
    """Create answers"""
    # get answers belonged to a question from user 
    # once got them, create each answer, corresponded to user_id, question_id, answer_id
    # show user the answers collected
    # if user has answer and wish
    # collect answer and wish
    # show user answers but place wish in other side (wish.html)
    # user has to be able to come back anytime to answer more questions or make more wishes
    # user will need a button that contains answers - wishes - respond questions or modificate
    # qids = request.form.getlist('question_id')
    
    for i, qid in enumerate(request.form.getlist('question_id')):
        answer = request.form.getlist('answer')[i]
        user_id = session.get("user_id")
        # question = crud.get_question_by_id(qid)

        if answer:
            print(qid, answer)
            a = model.Answer.query.filter_by(user_id=user_id, question_id=qid).first()
            print(a)
            if not a:
                new_answer = crud.create_answer(user_id, qid, answer)
                print(new_answer)
            else:
                updated_ans = model.Answer.query.filter_by(answer_id=a.answer_id).update({'answer': answer})
                print(updated_ans)
    flash("Your answers have been added")
    return redirect('/questions')
    
    #return redirect('/handle_answers/{answer_id}')  


@app.route('/questions/<question_id>')
def show_question(question_id):
    """Show details of the question"""

    question = crud.get_question_by_id(question_id)

    return render_template('question_details.html', question=question)

@app.route('/wish', methods=['POST'])
def register_wishes():
    """Create wishes"""

    

@app.route('/handle_answers/<answer_id>')
def show_answer(answer_id):
    """Show details of the question"""

    question = crud.get_question_by_id(question_id)
    answer = crud.get_answer_by_id(answer_id)

    return render_template('answer_details.html', answer=answer)
    






if __name__ == '__main__':
    model.connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)