from functools import wraps
from flask import g, request, redirect, url_for, session, abort, flash
import uuid
import logging

def generate_csrf_token():
    """Generates a new csrf token and adds it to the session

    Returns:
        Newly created csrf token
    """
    if '_csrf_token' not in session:
        session['_csrf_token'] = str(uuid.uuid4())
    return session['_csrf_token']


def check_csrf(f):
    """Deecorator function that check if a csrf token is valid"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.method == "POST":
            token = session.pop('_csrf_token', None)
            if not token or token != request.form.get('_csrf_token'):
                flash('Unauthorized')
                return redirect(url_for('catalogs.index'))

        return f(*args, **kwargs)
    return decorated_function
