from flask import Blueprint, render_template, abort

catalogs_api_app = Blueprint('catalogs_api', __name__)


@catalogs_api_app.route('/api/catalogs')
def index():
    return 'index catalogs'


@catalogs_api_app.route('/api/catalog')
def create():
    return 'create catalog'


@catalogs_api_app.route('/api/catalog', methods=['POST'])
def new():
    return 'new catalog'


@catalogs_api_app.route('/api/catalog/<id>/edit')
def edit(id):
    return 'edit catalog'


@catalogs_api_app.route('/api/catalog/<id>/edit', methods=['POST'])
def update(id):
    return 'update catalog'


@catalogs_api_app.route('/api/catalog/<id>')
def get(id):
    return 'get catalog'


@catalogs_api_app.route('/api/catalog/<id>', methods=['DELETE'])
def delete(id):
    return 'detele catalog'
