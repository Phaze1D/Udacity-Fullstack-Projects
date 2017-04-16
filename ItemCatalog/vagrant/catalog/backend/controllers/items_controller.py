from flask import Blueprint, render_template, abort, request, redirect, url_for
from backend.models import Item
from backend.models import Catalog
from backend.helpers import check_csrf, login_required, current_user, item_exists, item_belongs

import logging

items_app = Blueprint('items', __name__)

@items_app.route('/items')
def index(catalog_id=None):
    items = Item.get_all()
    return render_template('items/index.html', items=items)


@items_app.route('/item')
@items_app.route('/catalog/<catalog_id>/item')
@login_required
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
        return redirect(url_for('catalogs.get', id=item.catalog_id))


@items_app.route('/item/<id>/edit')
@login_required
@item_exists
@item_belongs
def edit(id):
    catalogs = Catalog.get_all()
    item = Item.find_by_id(id)
    return render_template('items/edit.html', item=item, catalogs=catalogs)


@items_app.route('/item/<id>/update', methods=['POST'])
@check_csrf
@login_required
@item_exists
@item_belongs
def update(id):
    form = request.form
    catalogs = Catalog.get_all()
    item, error = Item.edit(id=id,
                            name=form.get('name'),
                            description=form.get('description'),
                            catalog=Catalog.find_by_id(form.get('catalog_id')))

    if error:
        item = form.to_dict()
        item['id'] = id
        item['catalog_id'] = int(form.get('catalog_id'))
        return render_template('items/edit.html',
                                item=item,
                                catalogs=catalogs,
                                error=error)
    else:
        return redirect(url_for('items.get', id=item.id))


@items_app.route('/item/<id>')
@item_exists
def get(id):
    item=Item.find_by_id(id)
    return render_template('items/get.html', item=item)


@items_app.route('/item/<id>/delete', methods=['POST', 'GET'])
@check_csrf
@login_required
@item_exists
@item_belongs
def delete(id):
    item=Item.find_by_id(id)
    if request.method == "POST":
        Item.delete(item)
        return redirect(url_for('items.index'))
    else:
        return render_template('items/delete.html', item=item)
