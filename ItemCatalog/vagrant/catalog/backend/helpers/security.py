from functools import wraps
from flask import g, request, redirect, url_for, session, abort
import uuid
import logging

def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = str(uuid.uuid4())
    return session['_csrf_token']


def check_csrf(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.method == "POST":
            token = session.pop('_csrf_token', None)
            if not token or token != request.form.get('_csrf_token'):
                abort(403)

        return f(*args, **kwargs)
    return decorated_function
