"""CRUD operations"""

from model import db, User, Link, Question, Answer, Wish, connect_to_db



def create_user(email, password, name, gender):
    """Create a new user"""

    user = User(email=email, password=password, name=name, gender=gender)

    
    db.session.add(user)
    db.session.commit()

    return user


def  create_link(user_id1, user_id2):
    """Create a link to connect user1 and user2"""

    link = Link(user_id1=user_id1, user_id2=user_id2)

    db.session.add(link)
    db.session.commit()

    return link


def create_question(question):
    """Create a question"""

    question = Question(question=question)

    db.session.add(question)
    db.session.commit()

    return question

def get_questions():
    """Return all questions"""

    return Question.query.all()


def create_answer(question_id, answer, user_id):
    """Create and return an answer"""

    answer = Answer(question_id=question_id, answer=answer, user_id=user_id)

    db.session.add(answer)
    db.session.commit()

    return answer

def create_wishes(wish, user_id):
    """Create and return a wish from user"""

    wish = Wish(wish=wish, user_id=user_id)

    db.session.add(wish)
    db.session.commit()

    return wish


if __name__ == '__main__':
    from server import app
    connect_to_db(app)