from flask import Blueprint, render_template, abort


items_api_app = Blueprint('items_api', __name__)


@items_api_app.route('/api/catalog/<catalog_id>/items')
def index(catalog_id):
    return 'index items'


@items_api_app.route('/api/catalog/<catalog_id>/item')
def create(catalog_id):
    return 'create item'


@items_api_app.route('/api/catalog/<catalog_id>/item', methods=['POST'])
def new(catalog_id):
    return 'new item'


@items_api_app.route('/api/item/<id>/edit')
def edit(id):
    return 'edit item'


@items_api_app.route('/api/item/<id>/edit', methods=['POST'])
def update(id):
    return 'update item'


@items_api_app.route('/api/item/<id>')
def get(id):
    return 'get item'


@items_api_app.route('/api/item/<id>', methods=['DELETE'])
def delete(id):
    return 'detele item'
