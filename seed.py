
#import os
#import json
#from random import choice, randint
#from datetime import datetime

today = date.today()

#import crud
#import model
#import server

#os.system('dropdb forever')
#os.system('createdb forever')

model.connect_to_db(server.app)
model.db.create_all()




    user = User.query.options(db.joinedload('links')).all())

    for n in range(10):
        email = f'user{n}@test.com'
        password = 'test'

        user = crud.create_user(email, password, name, gender)

        



