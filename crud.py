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

# def get_link_by_partner(user_id):

#     return Link.query.filter_by(partner=user_id).first()

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

    return Question.query.get(question_id)


def create_answer(user, question, answer):
    """Create and return an answer"""

    answer = Answer(user=user, question=question, answer=answer)

    db.session.add(answer)
    db.session.commit()

    return answer


def get_answer():
    """Get answers from user"""

    answers = db.session.query(User.name, Question.question, Answer.answer).all()
    
    return answers

def get_answer_by_id(answer_id):
    """Return answers by primary key"""

    return Answer.query.get(answer_id)

def get_wish(wish):
    """Get wish from user_id"""

    wish = Answer(wish=wish)

    return wish


if __name__ == '__main__':
    from server import app
    connect_to_db(app)