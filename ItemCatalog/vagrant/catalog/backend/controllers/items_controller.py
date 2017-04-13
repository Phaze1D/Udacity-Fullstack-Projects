from flask import Blueprint, render_template, abort


items_app = Blueprint('items', __name__)


@items_app.route('/catalog/<catalog_id>/items')
def index(catalog_id):
    return 'index items'


@items_app.route('/catalog/<catalog_id>/item')
def create(catalog_id):
    return 'create item'


@items_app.route('/catalog/<catalog_id>/item', methods=['POST'])
def new(catalog_id):
    return 'new item'


@items_app.route('/item/<id>/edit')
def edit(id):
    return 'edit item'


@items_app.route('/item/<id>/edit', methods=['POST'])
def update(id):
    return 'update item'


@items_app.route('/item/<id>')
def get(id):
    return 'get item'


@items_app.route('/item/<id>', methods=['DELETE'])
def delete(id):
    return 'detele item'
