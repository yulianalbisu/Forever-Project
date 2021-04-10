

users = model.User.query.all() 
    #creating a link to get 2 users synchronized 

    #link1 = crud.create_link(users[1].user_id, users[2].user_id)
    #link2 = crud.create_link(users[3].user_id, users[4].user_id)
    #link3 = crud.create_link(users[5].user_id, users[6].user_id)
    #link4 = crud.create_link(users[7].user_id, users[8].user_id)
    #link5 = crud.create_link(users[9].user_id, users[10].user_id)

#second try

users = model.User.query.all() 

user_id1 = crud.create_user(email, password, name, gender)
user_id2 = crud.create_user(email, password, name, gender)

crud.create_link(user_id1, user_id2)