from flask import Blueprint, render_template, abort

catalogs_app = Blueprint('catalogs', __name__)


@catalogs_app.route('/catalogs')
def index():
    return 'index catalogs'


@catalogs_app.route('/catalog')
def create():
    return 'create catalog'


@catalogs_app.route('/catalog', methods=['POST'])
def new():
    return 'new catalog'


@catalogs_app.route('/catalog/<id>/edit')
def edit(id):
    return 'edit catalog'


@catalogs_app.route('/catalog/<id>/edit', methods=['POST'])
def update(id):
    return 'update catalog'


@catalogs_app.route('/catalog/<id>')
def get(id):
    return 'get catalog'


@catalogs_app.route('/catalog/<id>', methods=['DELETE'])
def delete(id):
    return 'detele catalog'
