import os
import json
from random import choice, randint

from model import db, User, Link, Question, Answer, connect_to_db
import crud
import server 

def create_example_data():
    #Users to populate user table

    user1 = User(email='user1@gmail.com', password='test1', name='Uno', nickname='One')
    db.session.add(user1)
    db.session.commit()

    user2 = User(email='user2@gmail.com', password='user2', name='Dos', nickname='Two')
    db.session.add(user2)
    db.session.commit()

    user3 = User(email='user3@gmail.com', password='user3', name='Tres', nickname='Three')
    db.session.add(user3)
    db.session.commit()

    user4 = User(email='user4@gmail.com', password='user4', name='Cuatro', nickname='Four')
    db.session.add(user4)
    db.session.commit()

    #Making links for users

    link1 = Link(link_id=1, user_id1=1, partner=2, anniversary="5/5/2017")
    db.session.add(link1)
    db.session.commit()

    link2 = Link(link_id=2, user_id1=3, partner=4, anniversary="12/5/2018")
    db.session.add(link2)
    db.session.commit()

    #Questions

    question1_user1 = Question(question_id=1, question="What's your favorite color?", category="personal", description="Colors are important because that can help you find, characteristics in your partner, as help you choose clothes, furniture and gifts.")
    db.session.add(question1_user1)
    db.session.commit()

    question2_user2 = Question(question_id=1, question="What's your favorite color?", category="personal", description="Colors are important because that can help you find, characteristics in your partner, as help you choose clothes, furniture and gifts.")
    db.session.add(question2_user2)
    db.session.commit()

    question3_user3 = Question(question_id=4, question="What's your favorite place?", category="personal", description="Some places would be for fun or only because they are beautiful, but some are meaningful depending of the stage of your partner's life.")
    db.session.add(question3_user3)
    db.session.commit()

    question4_user4 = Question(question_id=1, question="What's your favorite color?", category="personal", description="Colors are important because that can help you find, characteristics in your partner, as help you choose clothes, furniture and gifts.")
    db.session.add(question4_user4)
    db.session.commit()

    #Answering questions

    answer1_user1 = Answer(answer_id = 1, answer='red', wish='get me some ice-cream', question_id=1, user_id=1)
    db.session.add(answer1_user1)
    db.session.commit()

    answer2_user2 = Answer(answer_id = 2, answer='blue', wish='roundtrip', question_id=1, user_id=2)
    db.session.add(answer2_user2)
    db.session.commit()

    answer3_user3 = Answer(answer_id = 3, answer='Costa Rica', wish='dancing party', question_id=4, user_id=3)
    db.session.add(answer3_user3)
    db.session.commit()

    answer4_user4 = Answer(answer_id = 4, answer='green', wish='', question_id=1, user_id=4)
    db.session.add(answer4_user4)
    db.session.commit()




if __name__ == "__main__":
    os.system('dropdb testdb')
    os.system('createdb testdb')

    connect_to_db(server.app, db_uri='postgresql:///testdb')
    db.create_all()
    create_example_data()











if __name__ == '__main__':
    unittest.main()