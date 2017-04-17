from flask import Blueprint, render_template, abort, request, redirect, url_for, jsonify
from backend.models import Item
from backend.models import Catalog
from backend.helpers import check_csrf, login_required, current_user, item_exists, item_belongs

items_api_app = Blueprint('items_api', __name__)

@items_api_app.route('/api/items')
def index():
    items = [item.to_json() for item in Item.get_all()]
    return jsonify(items=items)


@items_api_app.route('/api/item/<id>')
@item_exists(json=True)
def get(id):
    item=Item.find_by_id(id)
    return jsonify(item.to_json())
