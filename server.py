"""Server for forever app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)

import random
import crud
from jinja2 import StrictUndefined
import model
from datetime import datetime, date

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined



@app.route('/') 
def homepage(): 
    """Show homepage with options to login and create an account"""


    return render_template('homepage.html') 

@app.route('/new-user')
def create_an_account():
    """Displays a form to create a new user"""

    return render_template('create_account.html')

@app.route('/login')
def display_login_form():
    """Display the form for loggin in"""

    return render_template('handle_login.html')

@app.route('/welcome') 
def welcome_users():
    """After login options to see another user, with same link key"""

    if 'user_id' in session:
        user=crud.get_user_by_id(session['user_id'])

    return render_template('welcome.html', user=user)


@app.route('/users/<user_id>')
def show_user(user_id):
    """Show details on a particular user"""
    # check if user_id passed in is user_id in session
    if 'user_id' in session:
        user = crud.get_user_by_id(user_id) #this may be user_id
        links = crud.get_links()
        

        for id, partner1, partner2 in links:
            if partner1 == user.user_id or partner2 == user.user_id:
                link = model.db.session.query(model.Link).get(id)
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
    nickname = request.form.get('nickname')
    anniversary = request.form.get('anniversary')

    user = crud.get_user_by_email(email) #in crud 
    
    if user:
        flash('Welcome!')
        # need to check if user is in session first, if not, redirect to /login
        return redirect(f'/users/{user.user_id}')
        
    else: #this for create account only
        new_user = crud.create_user(email, password, name)
        new_link = crud.create_link(anniversary, new_user.user_id) 
        flash('Account created! Please log in') 

        return redirect('/login') 

@app.route('/handle_login', methods=['POST'])
def login():
    """Existent user can login"""
 
    email = request.form.get('email')
    password= request.form.get('password')

    user = crud.get_user_by_email(email) 

    if user and user.password == password:
        session['user_id'] = user.user_id
        return redirect(f'/users/{user.user_id}') 
    else:
        flash('Wrong password')
        return redirect('/login') 


@app.route('/connecting')
def connecting_partner():


    return render_template('connecting_form.html')

@app.route('/connecting', methods=['POST'])
def register_partner():
    """Create partner from user_id1"""

    email = request.form.get('email')
    password= request.form.get('password')
    name = request.form.get('name')
    nickname = request.form.get('nickname')
    link_id = request.form.get('link_id')
    link_id = int(link_id)
    anniversary = request.form.get('anniversary')
    anniversary = datetime.strptime(anniversary, '%Y-%m-%d').strftime("%Y-%m-%d")
  
    user = crud.get_user_by_email(email) 

    if user:
        flash('Welcome!')
        
        return redirect(f'/users/{user.user_id}')
        
    else: 
        new_user = crud.create_user(email, password, name)
        flash('Account created! Please log in') 

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

@app.route('/tips')
def tips_for_user():
    """Getting some tips according to the questions"""

    questions = crud.get_questions()
    #return a tip when user ask for it randomnly
    


    return render_template('tips.html', questions=questions)


@app.route('/questions')
def all_questions():
    """View all questions"""

    if 'user_id' in session:
        user = crud.get_user_by_id(session['user_id'])
        questions = crud.get_questions()

        
        answers = {answer.question_id: answer.answer for answer in user.answers if answer.answer}
        

        ph = {}
        for q in range(1, len(questions) + 1):
            if answers.get(q): ph[q] = answers[q]
            else: ph[q] = ''

        return render_template('all_questions.html', questions=questions, answers=answers, ph=ph)
    
    else:
        return redirect('/login')   

@app.route('/handle_answers', methods=['POST'])
def register_answers():
    """Create answers"""
    
    user = crud.get_user_by_id(session['user_id'])
    answers = [] 
    for i, qid in enumerate(request.form.getlist('question_id')):
        answer = request.form.getlist('answer')[i]
       
        user_id = session.get("user_id")
        question = crud.get_question_by_id(qid) #getting all my question info
        q_text = crud.get_question_text_by_id(qid) #only getting the question text info
        answers.append([q_text, answer]) #this is line 9 in answer_details.html
        

        if answer:
            print(qid, answer)
            a = model.Answer.query.filter_by(user_id=user_id, question_id=qid).first()
            if not a:
                new_answer = crud.create_answer(user_id, qid, answer)
                
            else:
                updated_ans = model.Answer.query.filter_by(answer_id=a.answer_id).update({'answer': answer})
                
                model.db.session.commit()

    flash("Your answers have been added")
    

    return redirect('/show_answers') 
     

@app.route('/show_answers')
def show_answers():
    """Show the answers from user"""

    
    user = crud.get_user_by_id(session['user_id'])
    qids = [answer.question_id for answer in user.answers]
    answers = []
    for a in user.answers:
        q = crud.get_qtext_by_qid(a.question_id)
        if q:
            answers.append((q[0], q[1], a.answer))
    


    return render_template('showing_answers.html', answers=answers, user=user)



@app.route('/questions/<question_id>')
def show_question(question_id):
    """Show details of the question"""

    
    question = crud.get_question_by_id(question_id)

    return render_template('question_details.html', question=question)

@app.route('/wish')
def wishes_form():
    """Form to get wishes data"""


    return render_template('my_wishes.html')

@app.route('/wish', methods=['POST'])
def register_wishes():
    """Create wishes"""

    
    wish = request.form.get("wish")
   
    user = crud.get_user_by_id(session['user_id'])

    
    if wish:
        wish = crud.create_wish(wish, user)
        return render_template('show_wishes.html', wish=wish, user=user)

@app.route('/answers_partner')
def view_partner_answers():
    """User can view answers from partner"""

    user=crud.get_user_by_id(session['user_id'])
    

    if user:
        partner_id = crud.get_partner_by_user(user.user_id)
        

        if partner_id:
            partner = crud.get_user_by_id(partner_id)
            
            qids = [answer.question_id for answer in partner.answers]
            answers = []
            for a in partner.answers:
                q = crud.get_qtext_by_qid(a.question_id)
                if q:
                    answers.append((q[0], q[1], a.answer))
            
            return render_template('partner_answers.html', user=user, partner=partner, answers=answers)

        else:
            ("Your partner has not answered yet")   
            return redirect('/connecting')

    else:
        return redirect('/login')

    return jsonify([answers, qids])

@app.route('/wishes')
def view_user_wishes():
    """User can view wishes"""

    
    user = crud.get_user_by_id(session['user_id'])
    answers = crud.get_wish(user.user_id)

    if answers:
        
        return render_template('all_wishes.html', answers=answers, user=user)
    else:
        flash('Make a wish.')
        return redirect('/wish')

@app.route('/wishes_partner')
def view_partner_wishes():
    """ View partner wishes """

    user = crud.get_user_by_id(session['user_id'])
    

    if user:
        partnerid = crud.get_partner_by_user(user.user_id) #partner and user id, now if partner or user== show other partner wishes.
        

        if partnerid:
            partner = crud.get_user_by_id(partnerid)
             
            answers = crud.get_wish(partner.user_id)


            return render_template('partner_wishes.html', user=user, partner=partner, answers=answers)
        
        else:
            flash("You don't have a partner yet.")
            return redirect('/connecting')
    else:
        flash('Please log in or register for an account.')
        return redirect('/login')

@app.route('/checked_wishes')
def delete_wish_accomplished():
    """When user marks as done, wish is deleted"""

    partner_id = crud.get_partner_by_user(session['user_id'])

    delete_wish = request.args.get("wish")
    print('*******', wish, '********')
    
    #delete_wish = Answer.query.filter(Answer.wishes_checked).delete()
        #return redirect('/welcome')

@app.route('/logout')
def logout():
    """Log out user in session"""

    
    del session['user_id']
    print(session)
    flash("You have been logged out")


    return redirect('/')



if __name__ == '__main__':
    model.connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

