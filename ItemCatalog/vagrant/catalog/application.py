from flask import Flask, redirect, url_for
from backend.controllers import catalogs_app, items_app, users_app
from backend.api_controllers import catalogs_api_app, items_api_app
from backend.config import create_schema
from backend.helpers import generate_csrf_token, is_login
from backend.models import Catalog, Item, User


app = Flask(__name__, template_folder='frontend/templates', static_folder='frontend')
app.config.from_pyfile('config.cfg')
app.secret_key = app.config['SECRET_KEY']
app.jinja_env.globals['csrf_token'] = generate_csrf_token
app.jinja_env.globals['is_login'] = is_login

app.register_blueprint(catalogs_app)
app.register_blueprint(items_app)
app.register_blueprint(users_app)

app.register_blueprint(catalogs_api_app)
app.register_blueprint(items_api_app)

create_schema()

@app.route("/")
def root():
    return redirect(url_for('catalogs.index'))



if __name__ == "__main__":
    app.run(port=8080, host='0.0.0.0', debug=True)
