from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from grocery_app.models import User
from grocery_app.extensions import app

###########################
# Authentication
###########################

# authentication setup code

login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.init_app(app)

# This tells the login manager how to load a user with a particular id

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# initialize Bcrypt for hashing passwords:
bcrypt = Bcrypt(app)
