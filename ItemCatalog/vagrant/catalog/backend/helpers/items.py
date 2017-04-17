from functools import wraps
from flask import g, request, redirect, url_for, session, abort, flash, jsonify
from backend.models import Item

import logging

def item_exists(json=False):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            item = Item.find_by_id(kwargs.get('id'))
            if item == None:
                flash('Invalid Item id')
                if json:
                    return jsonify(error='Invalid Item id')
                else:
                    return redirect(url_for('items.index'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

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
