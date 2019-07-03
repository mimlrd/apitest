## core views.py

from flask import Blueprint, render_template, request
from api.models import Friend
from api.models import db
from flask_jwt import JWT, jwt_required, current_identity
from flask import jsonify



core_blueprint = Blueprint('core',
                           __name__ ,
                           template_folder='templates/core')


@core_blueprint.route('/', methods=['GET', 'POST'])
def home():
    ## info to reporte in the route
    if request.method == 'POST':
        fname = request.form['fname'];
        lname = request.form['lname'];
        age = request.form['age'];
        gender = request.form['gender'];

        ## create friend object
        friend = Friend(fname=fname.lower(), lname=lname.lower(),
                        age=int(age), gender=gender.lower())
        #print(friend.dict)

        ## save info to the database
        friend.save_to_db()


    return render_template('home.html')

# @core_blueprint.route('/friend_api')
# def get_friends():
#     return

@core_blueprint.route('/friends')
@jwt_required()
def get_friends():

    friends_quer = Friend.query_all()

    friends = [f.dict for f in friends_quer if f]
    return jsonify(friends)
