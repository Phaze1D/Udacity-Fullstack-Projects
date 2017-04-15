from functools import wraps
from flask import g, request, redirect, url_for, session, abort
from backend.models import User


def login(user):
    session['user'] = user.id

def is_login():
    return 'user' in session

def current_user():
    return User.find_by_id(session.get('user'))

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function
