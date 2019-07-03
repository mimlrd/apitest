#security.py

## create the security to authenticate users

from api.models import User
from flask_login import login_user
#from api import login_manager


def authenticate(username, password):
    ## need to retrieve user
    # usr = User.query.filter(db_and(User.username == username,
    #                                User.check_password(pwd)))
    print(username)

    ## 1 - check the user exist (is not none)
    usr = User.query.filter(User.username==username).first()
    #print(usr.username)
    ## 2 - check password math
    if usr.check_password(password) and usr is not None:
        #login_user(usr)
        return usr if usr else None

def identity(payload):
    user_id = payload['identity']
    return User.query.get_or_404(user_id)
