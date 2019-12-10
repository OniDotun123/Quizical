from flask import Blueprint, render_template

from .extensions import db
from .models import User, Question

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

@main.route('/login')
def login():
    render_template('/login.html')

@main.route('/question')
def question():
    render_template('/question.html')

@main.route('/register')
def register():
    render_template('/register.html')

@main.route('/unanswered')
def unanswered():
    render_template('/unanswered.html')

@main.route('/users')
def users():
    render_template('/users.html')

