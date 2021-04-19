"""Models for forever app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
from datetime import datetime, date




db = SQLAlchemy()


class User(db.Model):
    """The user's data"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    nickname = db.Column(db.String(20))

    partner = db.relationship('User', 
                                    secondary='links', 
                                    primaryjoin=('User.user_id==Link.user_id1'), 
                                    secondaryjoin=('User.user_id==Link.partner'))

 

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}  password={self.password} name={self.name} nickname={self.nickname}>'

class Link(db.Model):
    """Link a code to connect users"""

    __tablename__ = 'links'

    link_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id1 = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    partner = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    anniversary = db.Column(db.Date, default=date.today()) #anniversary

    #partner1 = db.relationship('User', foreign_keys=[user_id1]) RETURN ONLY USER NOT PARTNER
    #partner2 = db.relationship('User', foreign_keys=[partner])
    # def __repr__(self):
    #     return f'<Link link_id={self.link_id} anniversary={self.anniversary}>'

class Question(db.Model):
    """Form for user to answer"""

    __tablename__ = 'questions'

    question_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    question = db.Column(db.String)
    category = db.Column(db.String)
    description = db.Column(db.String)


    def __repr__(self):
        return f'<Question question_id={self.question_id} question={self.question}>'


class Answer(db.Model):
    """Answer from users in question's form"""

    __tablename__ = 'answers'

    answer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    answer = db.Column(db.String)
    wish = db.Column(db.String)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    user = db.relationship("User", backref='answers')
    question = db.relationship("Question", backref='answers')
    

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