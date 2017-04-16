from flask import Blueprint, render_template, abort, request, jsonify, redirect, url_for
from backend.models import Item
from backend.models import Catalog
from backend.helpers import check_csrf, login_required, catalog_exists

import logging

catalogs_app = Blueprint('catalogs', __name__)


@catalogs_app.route('/catalogs')
def index():
    catalogs = Catalog.get_all()
    return render_template('catalogs/index.html', catalogs=catalogs)


@catalogs_app.route('/catalog')
def create():
    return render_template('catalogs/create.html', catalog=None, error='')


@catalogs_app.route('/catalog', methods=['POST'])
@check_csrf
def new():
    catalog, error = Catalog.create(name=request.form.get('name'))
    if error:
        return render_template('catalogs/create.html',
                                catalog=request.form,
                                error=error)
    else:
        return redirect(url_for('catalogs.index'))


@catalogs_app.route('/catalog/<id>/edit')
@catalog_exists
def edit(id):
    catalog = Catalog.find_by_id(id)
    return render_template('catalogs/edit.html', catalog=catalog)


@catalogs_app.route('/catalog/<id>/update', methods=['POST'])
@check_csrf
@catalog_exists
def update(id):
    catalog, error = Catalog.edit(id=id, name=request.form.get('name'))
    if error:
        return render_template('catalogs/edit.html',
                                catalog=request.form,
                                error=error)
    else:
        return redirect(url_for('catalogs.index'))


@catalogs_app.route('/catalog/<id>')
@catalog_exists
def get(id):
    catalog = Catalog.find_by_id(id)
    return render_template('catalogs/get.html', catalog=catalog, items=catalog.items)
