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

def get_links():
    """Show the link"""

    return Link.query.all()


def create_link(link_id, anniversary):
    """Creates a link for users"""

    link = Link(anniversary=anniversary, user_id=user_id)

    
    db.session.add(link)
    db.session.commit()

def get_user_link(link_id):
    """Return a link for user"""

    return User.query.get(link_id)


def get_user_by_password(password):
    """Return a user by password"""

    return User.query.filter(User.password == password).first()


def create_question(question, description):
    """Create a question"""

    question = Question(question=question, description=description)

    db.session.add(question)
    db.session.commit()

    return question

def get_questions():
    """Return all questions"""

    return Question.query.all()

def get_question_by_id(question_id):
    """Return a question by primary key"""

    return Question.query.get(question_id)


def create_answer(user, question, answer, wish):
    """Create and return an answer"""

    answer = Answer(user=user, question=question, answer=answer, wish=wish)


    db.session.add(answer)
    db.session.commit()

    return answer



if __name__ == '__main__':
    from server import app
    connect_to_db(app)