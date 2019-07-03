## models.py

from api import db
import secrets
from api import login_manager, db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get_or_404(user_id)


class User(db.Model):
    ''' To create a user with credentials '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    hash_password = db.Column(db.String(256))
    email = db.Column(db.String(80), unique=True, nullable=False, index=True)
    dev_id = db.Column(db.String(80), unique=True, nullable=False, index=True)

    def __init__(self, email, username, pwd):
        self.email = email
        self.username = username.lower()
        self.hash_password = generate_password_hash(pwd)
        self.dev_id = secrets.token_hex(24)

    def json(self):
        return {'username': self.username,
                'email': self.email,
                'dev_id': self.dev_id }

    def __repr__(self):
        return f'Username: {self.username} and email: {self.email}'

    def check_password(self, pwd):
        return check_password_hash(self.hash_password, pwd)



class Friend(db.Model):

    __tablename__ = 'friends'

    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(80), nullable=False)
    fname = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(20), nullable=False, default='fml')


    def __init__(self, lname, fname, age, gender):
        self.lname = lname;
        self.fname = fname;
        self.age = age;
        self.gender = gender;
        ## for more info on @property please see following tutorial
        ## https://www.machinelearningplus.com/python/python-property/
    @property
    def fullname(self):
        return f"{self.fname.capitalize()} {self.lname.capitalize()}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split()
        self.lname = last
        self.fname = first


    @property
    def dict(self):

        return {
            'lname': self.lname,
            'fname': self.fname,
            'age': self.age,
            'gender': self.gender,
            'fulname': self.fullname
        }

    @classmethod
    def query_all(cls):
        return cls.query.all()

    
    def save_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
            raise ValueError('Sorry we coul not save the data at this time')



    def __repr__(self):
        return f"name: {self.fullname}"


# class Friend():
#
#     def __init__(self, lname, fname, age, gender):
#         self.lname = lname;
#         self.fname = fname;
#         self.age = age;
#         self.gender = gender;
#         self.fullname = self.full_name()
#         self.dict = {
#             'lname': self.lname,
#             'fname': self.fname,
#             'age': self.age,
#             'gender': self.gender,
#             'fulname': self.fullname
#         }
#
#     def full_name(self):
#         return f"{self.fname.capitalize()} {self.lname.capitalize()}"
#
#
#     def __repr__(self):
#         return f"name: {self.fullname}"
