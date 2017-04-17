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
