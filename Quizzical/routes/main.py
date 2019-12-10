from flask import Blueprint, render_template

from Quizzical.extensions import db
from Quizzical.models import Question

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('home.html')

@main.route('/ask')
def ask():
    return render_template('/ask.html')

@main.route('/answer')
def answer():
    return render_template('/answer.html')


@main.route('/question')
def question():
    return render_template('/question.html')



@main.route('/unanswered')
def unanswered():
    return render_template('/unanswered.html')

@main.route('/users')
def users():
    return render_template('/users.html')

@main.route('/home')
def home():
    return render_template('/home.html')

