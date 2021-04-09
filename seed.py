"""Script to seed the database"""


import os
import json
from random import choice, randint
from datetime import datetime

#today = date.today()

import crud
import model
import server

os.system('dropdb forever')
os.system('createdb forever')
model.connect_to_db(server.app)
model.db.create_all()

#loading the questions data!
with open('data/questions.json') as f:
    question_data = json.loads(f.read())


questions_in_db = []
for question in question_data:
    question = (question['question'])

    db_question = crud.create_question(question, answers)
        
    questions_in_db.append(db_question)


   # user = User.query.options(db.joinedload('links')).all())
for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'

    user = crud.create_user(email,password)

    #creating a link to get 2 users synchronized 
    for m in range(10):
        link = {m}
        user_id1 = f'{m}email, password'
        user_id2 = f'{m}email, password'

        link = crud.create_link(link, user_id1, user_id2)

    #creating an answer from users
    for _ in range(10):
        rendom_question = choice(questions_in_db)
        answer = randint(input["answer"]) #check if will work with input since user has to answer.

        crud.create_answer(user, random_question, answer)

    
        
        



