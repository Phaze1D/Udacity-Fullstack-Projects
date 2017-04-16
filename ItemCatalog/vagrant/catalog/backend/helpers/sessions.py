from functools import wraps
from flask import g, request, redirect, url_for, session, abort, flash
from backend.models import User

import logging

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
            flash('Must be logged in')
            return redirect(url_for('catalogs.index'))
        return f(*args, **kwargs)
    return decorated_function
