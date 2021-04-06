


class Users(db.Model):
    """The users"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(20))
    phone = db.Column(db.Integer, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    link_id = db.Column(db.Integer,
                        db.ForeignKey('link.link_id'),
                        nullable=False)

    link = db.relationship('Link', backref='users')

class Link(db.Model):

    __tablename__ = 'link'

    link_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False) #will get personal info?
    user2_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    date_rel = db.Column(db.DateTime) #should be a date
    users = db.relationship('Users', backref='link')

    users = db.relationship('Users', backref='user1_id')
    users = db.relationship('Users', backref='user2_id')
    answers = db.relationship('Answers', backref='user1_id')
    answers = db.relationship('Answers', backref='user2_id')
class Questions(db.Model):

    __tablename__ = 'questions'

    question_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    question = db.Column(db.String)

    answers = db.relationship('Answers', backref='questions')

class Answers(db.Model):

    __tablename__ = 'answers'

    answer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'))
    answer1 = db.Column(db.String, db.ForeignKey('link.user1_id'))
    answer2 = db.Column(db.String, db.ForeignKey('link.user2_id'))

