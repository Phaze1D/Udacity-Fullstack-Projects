from flask import Blueprint, render_template, abort, request
from backend.models import Item
from backend.models import Catalog
from backend.helpers import check_csrf, login_required, current_user

import logging

items_app = Blueprint('items', __name__)

@items_app.route('/items')
@items_app.route('/catalog/<catalog_id>/items')
def index(catalog_id):
    catalog = {}
    items = []
    return render_template('items/index.html', catalog=catalog, items=items)


@items_app.route('/item')
@items_app.route('/catalog/<catalog_id>/item')
def create(catalog_id=None):
    catalogs = ([Catalog.find_by_id(catalog_id)] if catalog_id
                else Catalog.get_all())
    return render_template( 'items/create.html',
                            item=None, error='', catalogs=catalogs)


@items_app.route('/item', methods=['POST'])
@check_csrf
@login_required
def new():
    form = request.form
    catalogs = Catalog.get_all()
    item, error = Item.create(  name=form.get('name'),
                                description=form.get('description'),
                                catalog=Catalog.find_by_id(form.get('catalog_id')),
                                user=current_user())
    if error:
        item = form.to_dict()
        item['catalog_id'] = int(form.get('catalog_id'))
        return render_template('items/create.html',
                                item=item,
                                catalogs=catalogs,
                                error=error)
    else:
        return redirect(url_for('catalogs.get', item.catalog_id))


@items_app.route('/item/<id>/edit')
def edit(id):
    catalogs = []
    item={}
    return render_template('items/edit.html', item=item, catalogs=catalogs)


@items_app.route('/item/<id>/edit', methods=['POST'])
@check_csrf
@login_required
def update(id):
    return 'update item'


@items_app.route('/item/<id>')
def get(id):
    item={}
    return render_template('items/get.html', item=item)


@items_app.route('/item/<id>', methods=['DELETE'])
def delete(id):
    return 'detele item'
