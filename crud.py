"""CRUD operations"""

from model import db, User, Link, Question, Answer, connect_to_db



def create_user(email, password, name):
    """Create a new user"""

    user = User(email=email, password=password, name=name)

    
    db.session.add(user)
    db.session.commit()

    return user

def get_users():
    """Return all users"""

    return User.query.all()

def get_user_by_id(user_id):
    """Return a user by ID"""

    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a user by email"""
#using this for login

    return User.query.filter(User.email == email).first()

def get_user_by_name(name):
    """Returns the name of the user"""

    return User.query.filter(User.name == name).first()

def get_anniversary(anniversary):
    """Return the date of anniversary"""

    return Link.query.filter(Link.anniversary == anniversary).first()


def create_link(anniversary, user_id):
    """Creates a link for users"""

    link = Link(anniversary=anniversary, user_id1=user_id)

    
    db.session.add(link)
    db.session.commit()

    return link

def get_links():
    """get a link and can be share with user"""

    #joining table users and links

    links = db.session.query(Link.link_id, Link.user_id1, Link.partner).all()
    return links


def get_link_by_link_id(link_id):
    """validating partner"""

    return db.session.query(Link).filter_by(link_id=link_id).first()

def update_partner_link(link_id, user_id):
    """update partner link"""

    link = db.session.query(Link).filter_by(link_id=link_id).update({'partner': user_id})
    db.session.commit()

    return link


def get_user_by_password(password):
    """Return a user by password"""

    return User.query.filter(User.password == password).first()


def create_question(category, question, description):
    """Create a question"""

    question = Question(category=category, question=question, description=description)

    db.session.add(question)
    db.session.commit()

    return question

def get_questions():
    """Return all questions"""

    return Question.query.all()

def get_question_by_question(question):
    """Show all questions by question"""

    return Question.query.filter(Question.question == question) #just made this to get the question printed in html

def question_category_personal():
    """Return questions by category personal"""

    category_personal = db.session.query(Question).filter_by(category='personal').all()
    

    db.session.add(category_personal)
    db.session.commit()

    return category_personal

def question_category_love():
    """Return questions by category love"""

    category_love = db.session.query(Question).filter_by(category='love language').all()
    
    db.session.add(category_love)
    db.session.commit()

    return category_love

def question_category_family():
    """Return questions by category family"""

    category_family = db.session.query(Question).filter_by(category='family').all()

    db.session.add(category_family)
    db.session.commit()

    return category_family

def get_question_by_id(question_id):
    """Return a question by primary key"""

    return Question.query.filter_by(question_id=question_id).first()

def get_qtext_by_qid(qid):
    return db.session.query(Question.question_id, Question.question).filter_by(question_id=qid).first()

def get_question_text_by_id(question_id):
    """Get only the text of the questions"""

    question = Question.query.get(question_id)

    return question.question

def create_answer(user_id, question_id, answer):
    """Create and return an answer"""

    answer = Answer(user_id=user_id, question_id=question_id, answer=answer)

    db.session.add(answer)
    db.session.commit()

    return answer


def get_answer():
    """Get answers from user"""

    answers = db.session.query(User.name, Question.question, Answer.answer).all()
    
    return answers

def get_answer_by_id(user_id):
    """Return answers by primary key"""

    return db.session.query(Answer).filter_by(user_id=user_id).all()


def get_answers_answered(user_id):
    """Return only answers answered"""

    return db.session.query(Answer.answer, Question.question).filter(Answer.answer_id==Question.question_id).filter(Answer.answer.isnot(None)).filter_by(user_id=user_id).all()

def create_wish(wish,user):
    """Create a wish"""

    wish = Answer(wish=wish, user=user)

    db.session.add(wish)
    db.session.commit()

    return wish


def get_wish(user_id):
    """Get wish from user"""

    return db.session.query(Answer).filter(Answer.wish.isnot(None)).filter_by(user_id=user_id).all()

def get_partner_by_user(user_id):
    """Returns user_id1, partner1"""
    try:
        link1 = db.session.query(Link).filter_by(user_id1=user_id).first()
        link2 = db.session.query(Link).filter_by(partner=user_id).first()
        return link1.partner if link1 else link2.user_id1
    except:
        return None



def get_user_wishes(user_id):
    """Getting partner1"""

    #wish_userid1 = db.session.query(Answer.wish, Link.user_id1).filter(Answer.wish.isnot(None)).first()
    return db.session.query(Answer.wish).filter_by(user_id=user_id).all()


def get_both_partners_id():
    """Returns user's pairs"""

    partners= db.session.query(Link.user_id1, Link.partner)
    
    return partners.first()


    
if __name__ == '__main__':
    from server import app
    connect_to_db(app)