"""Script to seed the database"""


import os
import json
from faker import Faker
from random import choice, randint
from datetime import datetime


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
    question, description = (question['category'],
                            question['question'],
                            question['description'])
    
    db_question = crud.create_question(category, question, description)
        
    questions_in_db.append(db_question)


genders = ['woman', 'man', 'no answer']
for user in range(10):
    email = fake.email()
    password = fake.password()
    name = fake.name()
    gender = choice(genders)

    user = crud.create_user(email, password, name, gender)

    #creating an answer from users
    for _ in range(10):
        random_question = questions_in_db
        answer = fake.text() #check if will work with input since user has to answer.
        wish = fake.sentence()

        crud.create_answer(user, random_question, answer, wish)

    for link in range(10):
        link = link_id
        anniversary = date.today()

        crud.create_link(user, link, anniversary)




    
        
        



