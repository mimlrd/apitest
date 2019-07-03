## app.py
import os
from api import create_app
from flask_restful import Api, Resource
from flask import jsonify
#from api.api_models import FriendApi, AddFriend
## for authentication of the api
from flask_jwt import JWT, jwt_required, current_identity
from api.security import authenticate, identity
from api.models import Friend




app = create_app(os.getenv('FLASK_CONFIG') or 'default')

my_api = Api(app)
jwt = JWT(app,authenticate, identity)

@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity


@app.route('/all_friends')
@jwt_required()
def get_all_friends():

    friends_quer = Friend.query_all()

    friends = [f.dict for f in friends_quer if f]
    return jsonify(friends)

# @jwt.error_handler
# def customized_error_handler(error):
#     return jsonify({
#                        'message': error.description,
#                        'code': error.status_code
#                    }), error.status_code

class AllFriends(Resource):

    @jwt_required
    def get(self, name):
        str_1 = f"Hey {name} This is working fine!"
        return {'message':str_1}

my_api.add_resource(AllFriends, '/api/<string:name>')


######################################
##                                  ##
##    import the blueprints here!   ##
##                                  ##
######################################

from api.core.views import core_blueprint


######################################
##                                  ##
##    Register blueprints here!     ##
##                                  ##
######################################

app.register_blueprint(core_blueprint)




if __name__ == '__main__':
    ## we add the resource to the api, with the url endpoint to access the
    ## data
    from api.friend_resources import FriendApi, AddFriend
    my_api.add_resource(FriendApi, '/api_2.0')
    ## a new resource to let user add friends
    my_api.add_resource(AddFriend, '/add_friend')



    app.run(host='0.0.0.0', debug=True)
