from flask import Blueprint, render_template, abort


items_app = Blueprint('items', __name__)

@items_app.route('/items')
@items_app.route('/catalog/<catalog_id>/items')
def index(catalog_id):
    catalog = {}
    items = []
    return render_template('items/index.html', catalog=catalog, items=items)


@items_app.route('/item')
def create():
    catalogs = []
    return render_template('items/create.html', catalogs=catalogs)


@items_app.route('/item', methods=['POST'])
def new():
    return 'new item'


@items_app.route('/item/<id>/edit')
def edit(id):
    catalogs = []
    item={}
    return render_template('items/edit.html', item=item, catalogs=catalogs)


@items_app.route('/item/<id>/edit', methods=['POST'])
def update(id):
    return 'update item'


@items_app.route('/item/<id>')
def get(id):
    item={}
    return render_template('items/get.html', item=item)


@items_app.route('/item/<id>', methods=['DELETE'])
def delete(id):
    return 'detele item'
