from flask import session
import uuid

def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = uuid.uuid4()
    return session['_csrf_token']
