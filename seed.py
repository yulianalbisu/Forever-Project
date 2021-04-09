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

    #for n in range(10):
        #email = f'user{n}@test.com'
        #password = 'test'

        #user = crud.create_user(email, password, name, gender)

        



