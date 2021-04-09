"""Script to seed the database"""


import os
import json
from faker import Faker
from random import choice, randint
from datetime import datetime

#today = date.today()

import crud
import model
import server

fake = Faker()

os.path.realpath('.') #added to find my script
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
    

    db_question = crud.create_question(question)
        
    questions_in_db.append(db_question)


   # user = User.query.options(db.joinedload('links')).all())
for n in range(10):
    email = fake.email()
    password = fake.password()
    name = fake.name()
    gender = fake.text()

    user = crud.create_user(email, password, name, gender)

users = User.query.all() 
    #creating a link to get 2 users synchronized 
crud.create_link(users[0].user_id1, users[1].user_id2)
crud.create_link(users[2].user_id1, users[3].user_id2)
crud.create_link(users[4].user_id1, users[5].user_id2)
crud.create_link(users[6].user_id1, users[7].user_id2)
crud.create_link(users[8].user_id1, users[9].user_id2)
crud.create_link(users[10].user_id1, users[11].user_id2)
    

    #creating an answer from users
for _ in range(10):
    random_question = choice(questions_in_db)
    answer = fake.text() #check if will work with input since user has to answer.
    user = user
    
    crud.create_answer(user, random_question, answer)

for w in range(10):
    wish = fake.text()
    user = user
    
    crud.create_wishes(wish, user)



    
        
        



