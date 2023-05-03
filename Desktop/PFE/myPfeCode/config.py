

from app import create_app
app = create_app()
app.config['SECRET_KEY'] = b'(\x8f\x16\xbe$l\xdd\xe7]\xf9&\xd3\xd12x\xb0'
import pymongo 
client = pymongo.MongoClient('localhost',27017)
db1= client.genetic_system