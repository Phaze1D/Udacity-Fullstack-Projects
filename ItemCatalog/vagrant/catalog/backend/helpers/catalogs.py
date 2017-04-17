from functools import wraps
from flask import g, request, redirect, url_for, session, abort, flash, jsonify
from backend.models import Catalog


def catalog_exists(json=False):
    """ Decorator function that checks if a catalog id is valid

    Note:
        Function should be use whenever a catalog id is pass

    Args:
        json(boolean): Whether to return a json obect or redirect

    Returns:
        A redirect or a jsonify object
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            catalog = Catalog.find_by_id(kwargs.get('id'))
            if catalog == None:
                flash('Invalid Catalog id')
                if json:
                    return jsonify(error='Invalid Catalog id')
                else:
                    return redirect(url_for('catalogs.index'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def catalog_belongs(f):
    """ Decorator function that checks if a catalog id belongs to the current user

    Note:
        Function should be use whenever a catalog id is pass

    Returns:
        A redirect with a flash if catalog does not belong to the current user
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        item = Catalog.find_by_id(kwargs.get('id'))
        if item.user_id is not session.get('user'):
            flash('Unauthorized')
            return redirect(url_for('catalogs.index'))
        return f(*args, **kwargs)
    return decorated_function
