from functools import wraps
from flask import g, request, redirect, url_for, session, abort, flash
from backend.models import User

import logging

def login(user):
    """Logs in a user"""
    session['user'] = user.id

def is_login():
    """Check if a user is logged in"""
    return 'user' in session

def current_user():
    """Gets the current logged in user"""
    return User.find_by_id(session.get('user'))

def login_required(f):
    """Decorator function that checks if a user is logged in"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_login():
            flash('Must be logged in')
            return redirect(url_for('catalogs.index'))
        return f(*args, **kwargs)
    return decorated_function
