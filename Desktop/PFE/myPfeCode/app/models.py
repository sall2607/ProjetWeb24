from flask_login import LoginManager
from flask_login import UserMixin
from flask import session ,jsonify

from . import db1



#class User(UserMixin, db.Model):
class User(UserMixin):
    
    def __init__ (self, user_json):
        self.user_json = user_json

    def get_id(self):
        object_id= self.user_json.get('_id')
        return str(object_id)
    def query(user_id):
        r=db1.users.find({ '_id': user_id})
        return r 



    