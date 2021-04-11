"""Models for forever app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime




db = SQLAlchemy()


class User(db.Model):
    """The user's data"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(20))

    answer = db.relationship('Answer', backref= 'users')

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}  password={self.password} name={self.name} gender={self.gender}>'

class Link(db.Model):
    """Link a code to connect users"""

    __tablename__ = 'links'

    link_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    anniversary = db.Column(db.DateTime, default=datetime.now()) #anniversary
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    user = db.relationship('User', backref='links')


    def __repr__(self):
        return f'<Link link_id={self.link_id} anniversary={self.anniversary}>'

class Question(db.Model):
    """Form for user to answer"""

    __tablename__ = 'questions'

    question_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    question = db.Column(db.String)
    description = db.Column(db.Text)
    answer = db.relationship('Answer', backref='questions')

    def __repr__(self):
        return f'<Question question_id={self.question_id} question={self.question}>'


class Answer(db.Model):
    """Answer from users in question's form"""

    __tablename__ = 'answers'

    answer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    answer = db.Column(db.String)
    wish = db.Column(db.Integer)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    

    def __repr__(self):
        return f'<Answer answer_id={self.answer_id} answer={self.answer} wish={self.wish}>'  


def connect_to_db(flask_app, db_uri='postgresql:///forever', echo=False): #i change echo to false
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    

    db.app = flask_app
    db.init_app(flask_app)
    #db.drop_all()
    #db.create_all()


    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)