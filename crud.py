"""CRUD operations"""

from model import db, User, Movie, Rating, connect_to_db

if __name__ == '__main__':
    from server import app
    connect_to_db(app)


new_user = User(email=email, password=password)

db.session.add(new_user)
db.session.commit()


new_link = Link(link_id=link_id, user_id=user_id, date_rel=date_rel)

db.session.add(new_link)
db.session.commit()


new_question = Question(question_id=question_id, question=question, answers=answer)

db.session.add(new_question)
db.session.commit()

new_answer = Answer(answer_id=answer_id, question=new_question, answer=new_answer, user=new_user, link=new_link)

db.session.add(new_answer)
db.session.commit()

