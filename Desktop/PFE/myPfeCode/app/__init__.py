from flask import Flask ,jsonify ,json
from flask_login import LoginManager
import pymongo 
client = pymongo.MongoClient('localhost',27017)
db1= client.genetic_system
from datetime import datetime , date 
#import isodate as iso 
from bson import ObjectId
from flask.json import JSONEncoder
from werkzeug.routing import BaseConverter

class MongoJSONEencoder(JSONEncoder):
    def default(self, o) :
        #if isinstance (o, (datetime , date)):
            #return iso.datetime_isoformat(o)
        if isinstance(o, ObjectId):
            return str(o)
        else:
            return super().default(o) 
        
class ObjectIdConverter(BaseConverter):
    def to_python(self, value):
        return ObjectId(value)
    def to_url(self, value):
        return str(value)


def create_app():
    app = Flask(__name__)
    
    app.json_encoder=MongoJSONEencoder
    app.url_map.converters['objectid']=ObjectIdConverter
    client = pymongo.MongoClient('localhost',27017)
    db1= client.genetic_system
    app.config.from_object('config')
    app.config['SECRET_KEY'] = b'657d6b8c87fb81ab108dc12cb9bdc5bc8ec46e4b663ef43f9391c9a373c608d4'
    
    #db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User 

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        #return User.query.get(int(user_id))
        user_json = db1.users.find_one({'_id': ObjectId(user_id)})
        return User(user_json)
            
        
    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
