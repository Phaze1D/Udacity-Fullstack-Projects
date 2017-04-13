from flask import Blueprint, render_template, abort

catalogs_app = Blueprint('catalogs', __name__)


@catalogs_app.route('/catalogs')
def index():
    catalogs = []
    return render_template('catalogs/index.html', catalogs=catalogs)


@catalogs_app.route('/catalog')
def create():
    return render_template('catalogs/create.html')


@catalogs_app.route('/catalog', methods=['POST'])
def new():
    return 'new catalog'


@catalogs_app.route('/catalog/<id>/edit')
def edit(id):
    catalog={}
    return render_template('catalogs/edit.html', catalog=catalog)


@catalogs_app.route('/catalog/<id>/edit', methods=['POST'])
def update(id):
    return 'update catalog'


@catalogs_app.route('/catalog/<id>')
def get(id):
    catalog={}
    return render_template('catalogs/get.html', catalog=catalog)


@catalogs_app.route('/catalog/<id>', methods=['DELETE'])
def delete(id):
    return 'detele catalog'
