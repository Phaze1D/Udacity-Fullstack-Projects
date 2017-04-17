from flask import Blueprint, render_template, abort, request, jsonify, redirect, url_for
from backend.models import Item
from backend.models import Catalog
from backend.helpers import check_csrf, login_required, catalog_exists, catalog_belongs, current_user


catalogs_app = Blueprint('catalogs', __name__)


@catalogs_app.route('/catalogs')
def index():
    """Function that returns html template with all the catalogs"""
    catalogs = Catalog.get_all()
    return render_template('catalogs/index.html', catalogs=catalogs)


@catalogs_app.route('/catalog')
@login_required
def create():
    """Function that returns html template with the catalog create form"""
    return render_template('catalogs/create.html', catalog=None, error='')


@catalogs_app.route('/catalog', methods=['POST'])
@check_csrf
@login_required
def new():
    """Function that adds a new catalog into the database or rerenders
    the catalog create form
    """
    catalog, error = Catalog.create(name=request.form.get('name'),
                                    user=current_user())
    if error:
        return render_template('catalogs/create.html',
                                catalog=request.form,
                                error=error)
    else:
        return redirect(url_for('catalogs.index'))


@catalogs_app.route('/catalog/<id>/edit')
@login_required
@catalog_exists()
@catalog_belongs
def edit(id):
    """Function that returns html template with the catalog edit form"""
    catalog = Catalog.find_by_id(id)
    return render_template('catalogs/edit.html', catalog=catalog)


@catalogs_app.route('/catalog/<id>/update', methods=['POST'])
@check_csrf
@login_required
@catalog_exists()
@catalog_belongs
def update(id):
    """Function that updates a catalog into the database or rerenders
    the catalog edit form
    """
    catalog, error = Catalog.edit(id=id, name=request.form.get('name'))
    if error:
        return render_template('catalogs/edit.html',
                                catalog=request.form,
                                error=error)
    else:
        return redirect(url_for('catalogs.index'))


@catalogs_app.route('/catalog/<id>')
@catalog_exists()
def get(id):
    """Function that returns html template with the catalog information"""
    catalog = Catalog.find_by_id(id)
    return render_template('catalogs/get.html', catalog=catalog, items=catalog.items)
