"""Models for forever app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class User(db.Model):
    """The users data"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(20))
    phone = db.Column(db.Integer, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    link_id = db.Column(db.Integer,
                        db.ForeignKey('links.link_id'),
                        nullable=False)
    

    link = db.relationship('Link')
    answers = db.relationship('Answer') ##this relationship is with my primary key, connected by name?

    #def __repr__(self):

class Link(db.Model):
    """Link a code to connect couple"""

    __tablename__ = 'links'

    link_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False) #will get personal info?
    user2_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    date_rel = db.Column(db.DateTime) #should be a date

    
    users = db.relationship('User')
    answers = db.relationship('Answer')

    #def __repr__(self):

class Question(db.Model):
    """Form for user to answer"""

    __tablename__ = 'questions'

    question_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    question = db.Column(db.String)
    
    answers = db.relationship('Answer')

    #def __repr__(self):


class Answer(db.Model):
    """Answer from question's form"""

    __tablename__ = 'answers'

    answer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'))
    answer = db.Column(db.String ) ## 2 items, same foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    questions = db.relationship('Question')
    users = db.relationship('User')

    #def __repr__(self):

def connect_to_db(flask_app, db_uri='postgresql:///my_forever', echo=False):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app, echo=False)