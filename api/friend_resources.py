## API Models api_models.py

from flask import request
from flask import jsonify, make_response

#from api import create_app
#from api import db

from flask_marshmallow import Marshmallow


# app = create_app('default')
# app.app_context().push()

from app import app
app.app_context().push()
from flask_restful import Resource
from flask_jwt import jwt_required
from api.models import Friend


#from api.models import Friend
# from app import app
# ma = Marshmallow(app)
#
# class FriendSchema(ma.Schema):
#     class Meta:
#         fields = ('lname','fname','age','gender')

# friend_shema = FriendSchema()
# friends_shema = FriendSchema(many=True)



class FriendApi(Resource):
    ''' A class that will let users to get
        friends from the api

        '''
    #decorators = [jwt_required]
    #from app import app

    ## we start by creating some friends manually
    # sarah = Friend(fname='Sarah', lname='Daly', age=45, gender='female')

    ##print(friends_quer)

    #print(friends)

    # result = friends_shema.dump(friends)
    # print(type(result.data))


    ## send the list of friends back to the appi
    @jwt_required
    def get(self):
        ## get the friends list
        print("------------------------")
        friends_quer = Friend.query_all()

        friends = [f.dict for f in friends_quer if f]
        return jsonify(friends)


    def post(self):
        # print(friend_info)
        ## to get the data in the body
        request_data = request.get_json()
        print(request_data)

        self.lname = request_data['lname']
        self.fname = request_data['fname']
        self.age = request_data['age']
        self.gender = request_data['gender']


        friend = Friend(fname=self.fname.lower(),
                        lname=self.lname.lower(),
                        age=int(self.age),
                        gender=self.gender.lower())

        friend.save_to_db()
        # db.session.add(friend)
        # db.session.commit()

        return jsonify({"message": "success"})



class AddFriend(Resource):
    ''' A class that will let user to add friend through the api '''
    ######################################
    ##                                  ##
    ##    set a value to the database   ##
    ##                                  ##
    ######################################
    ## using the wrapper jwt_required to make that only
    ## authenticate users could access
    pass

    # @jwt_required
    # def post(self):
    #     # print(friend_info)
    #     ## to get the data in the body
    #     request_data = request.get_json()
    #     print(request_data)
    #
    #     self.lname = request_data['lname']
    #     self.fname = request_data['fname']
    #     self.age = request_data['age']
    #     self.gender = request_data['gender']
    #
    #
    #     friend = Friend(fname=self.fname.lower(),
    #                     lname=self.lname.lower(),
    #                     age=int(self.age),
    #                     gender=self.gender.lower())
    #
    #     db.session.add(friend)
    #     db.session.commit()
    #
    #     return jsonify({"message": "success"})
