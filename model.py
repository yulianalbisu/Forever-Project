"""Models for forever app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class User(db.Model):
    """The users data"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String(20))
    gender = db.Column(db.String(20))
    
    

    links = db.relationship('Link')
    answers = db.relationship('Answer') ##this relationship is with my primary key, connected by name?

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

class Link(db.Model):
    """Link a code to connect couple"""

    __tablename__ = 'links'

    link_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False) #user1 should connect by link to user2
    user2_id = db.Column(db.Integer)
    date_rel = db.Column(db.DateTime) #should be a date

    
    users = db.relationship('User')
    answers = db.relationship('Answer')

    def __repr__(self):
        return f'<Link link_id={self.link_id}>'

class Question(db.Model):
    """Form for user to answer"""

    __tablename__ = 'questions'

    question_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    question = db.Column(db.String)
    
    answers = db.relationship('Answer')

    def __repr__(self):
        return f'<Question question_id={self.question_id} question={self.question}>'


class Answer(db.Model):
    """Answer from question's form"""

    __tablename__ = 'answers'

    answer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'))
    answer = db.Column(db.String ) ## 2 items, same foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    link_id = db.Column(db.Integer, db.ForeignKey('links.link_id'))

    questions = db.relationship('Question')
    users = db.relationship('User')
    links = db.relationship('Link')

    def __repr__(self):
        return f'<Answer answer_id={self.answer_id} answer={self.answer}>'


def connect_to_db(flask_app, db_uri='postgresql:///forever', echo=False):
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