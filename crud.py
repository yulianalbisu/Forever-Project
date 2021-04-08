"""CRUD operations"""

from model import db, User, Link, Question, Answer, connect_to_db


def create_user(email, password):

    new_user = User(email=email, password=password)

    db.session.add(new_user)
    db.session.commit()

    return new_user

def  create_link(user_id1, user_id2, date):
link = Link(link_id=link_id, user=user_id1, user=user_id2, date_rel=date_rel)

db.session.add(link)
db.session.commit()


def create_question(question_id, question, answer):
    """Create and return an answer"""

question = Question(question_id=question_id, question=question, answers=answer)

db.session.add(question)
db.session.commit()

def create_answer(answer_id, question, answer, user, link)

answer = Answer(answer_id=answer_id, question=question, answer=answer, user=user, link=link)

db.session.add(answer)
db.session.commit()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)