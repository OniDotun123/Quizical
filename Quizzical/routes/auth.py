from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user

from Quizzical.extensions import db
from Quizzical.models import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        user = User.query.filter_by(name=name).first()

        error_message = ''

        if not user or not check_password_hash(user.password, password):
            error_message = 'Could not login. Please try again'
        
        if not error_message: 
            login_user(user)
            return redirect(url_for('main.index'))
            

    return render_template('login.html')



#register logic below. Make sure to be aware of admin and expert settings. This determines the type of user that will be created. 
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        unhashed_password = request.form['password']

        user = User(
            name=name, 
            unhashed_password=unhashed_password, 
            admin=True, 
            expert=False
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    return render_template('/register.html')


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))