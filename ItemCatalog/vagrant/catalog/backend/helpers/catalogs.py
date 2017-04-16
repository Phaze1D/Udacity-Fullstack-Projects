from functools import wraps
from flask import g, request, redirect, url_for, session, abort, flash
from backend.models import Catalog


def catalog_exists(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        catalog = Catalog.find_by_id(kwargs.get('id'))
        if catalog == None:
            flash('Invalid Catalog id')
            return redirect(url_for('catalogs.index'))
        return f(*args, **kwargs)
    return decorated_function
