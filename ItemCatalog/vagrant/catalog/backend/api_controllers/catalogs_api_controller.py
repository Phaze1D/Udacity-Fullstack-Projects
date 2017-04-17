from flask import Blueprint, render_template, abort, request, jsonify, redirect, url_for
from backend.models import Item
from backend.models import Catalog
from backend.helpers import check_csrf, login_required, catalog_exists


catalogs_api_app = Blueprint('catalogs_api', __name__)


@catalogs_api_app.route('/api/catalogs')
def index():
    catalogs = [catalog.to_json() for catalog in Catalog.get_all()]
    return jsonify(catalogs=catalogs)



@catalogs_api_app.route('/api/catalog/<id>')
@catalog_exists
def get(id):
    catalog = Catalog.find_by_id(id)
    return jsonify(catalog.to_json())
