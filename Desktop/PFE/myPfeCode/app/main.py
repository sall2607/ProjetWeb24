from flask import Blueprint , render_template , session , redirect ,request , url_for,jsonify
from flask_login import login_required, current_user
from . import db1

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@main.route('/profile', methods=['POST'])
def profile_post():
    fichier = request.form.get('file')

    return redirect(url_for('main.profile'))

@main.route('/recherche')
@login_required
def recherche():
    return render_template('recherche.html')  

def start_session( user):
      
        session['logged_in']=True
        session['user']=user
        return jsonify(user) , 200
@main.route('/recherche', methods=['POST'])
def recherche_post():
    choix = request.form.get('recherche')
    res= db1.maladies.find_one({'nomMaladie':choix})
    start_session( res)
    return redirect(url_for('main.recherche'))
