from flask import Blueprint, render_template, abort

users_app = Blueprint('users', __name__)


@users_app.route('/signup')
def create():
    return 'signup'


@users_app.route('/signup',  methods=['POST'])
def new():
    return 'signup'


@users_app.route('/login')
def login():
    return 'login'


@users_app.route('/login',  methods=['POST'])
def logout():
    return 'logout'
