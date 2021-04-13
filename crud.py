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

    return User.query.filter(User.email == email).first()

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


def  create_link(link_id, anniversary):
    """Create a link to connect user1 and user2"""

    link = Link(link_id=link_id, anniversary=anniversary, user=user)

    db.session.add(link)
    db.session.commit()

    return link





def create_answer(user, question, answer, wish):
    """Create and return an answer"""

    answer = Answer(user=user, question=question, answer=answer, wish=wish)


    db.session.add(answer)
    db.session.commit()

    return answer



if __name__ == '__main__':
    from server import app
    connect_to_db(app)