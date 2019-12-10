from flask import Blueprint, render_template, redirect, url_for, request

from Quizzical.extensions import db
from Quizzical.models import User

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('/login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        unhashed_pass = request.form['password']

        user = User(
            name=name, 
            unhashed_pass=unhashed_pass, 
            admin=True, 
            expert=False
        )

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('/register.html')