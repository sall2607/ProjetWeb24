from flask import Blueprint , render_template, flash , redirect, url_for , request ,session ,jsonify 
from . import db1
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from flask_login import login_user , logout_user, login_required , login_manager
import uuid
from bson import ObjectId
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('sign-up.html')

@auth.route('/logout')
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('main.index'))

def start_session( user):
        del user['password']
        session['logged_in']=True
        session['user']=user
        return jsonify(user) , 200


@auth.route('/signup', methods=['POST'])
def signup_post():
    use = {
        "id": uuid.uuid4().hex,
        "name":request.form.get('name') ,
        "email":request.form.get('email'),
        "password": request.form.get('password')
    }
    use['password']=generate_password_hash(use['password'], method='sha256')

    
    if db1.users.find_one({"email":use['email']}):
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))


    # add the new user to the database
    db1.users.insert_one(use)
    # code to validate and add user to database goes here
    flash('Inscription réussie')
    return redirect(url_for('auth.login'))

...
@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    #user = User.query.filter_by(email=email).first()

    user=db1.users.find_one({"email":email})

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    #if not user or not check_password_hash(user['password], password):
    if not user or not check_password_hash(user['password'], password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
   
   
    start_session(user)
    loginuser= User(user)
    login_user(loginuser, remember=remember)
    return redirect(url_for('main.profile'))

