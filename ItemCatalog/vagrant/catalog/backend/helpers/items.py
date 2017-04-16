from functools import wraps
from flask import g, request, redirect, url_for, session, abort, flash
from backend.models import Item

import logging

def item_exists(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        item = Item.find_by_id(kwargs.get('id'))
        if item == None:
            flash('Invalid Item id')
            return redirect(url_for('items.index'))
        return f(*args, **kwargs)
    return decorated_function

def item_belongs(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        item = Item.find_by_id(kwargs.get('id'))
        logging.warning(session.get('user'))
        if item.user_id is not session.get('user'):
            flash('Unauthorized')
            return redirect(url_for('items.index'))
        return f(*args, **kwargs)
    return decorated_function
