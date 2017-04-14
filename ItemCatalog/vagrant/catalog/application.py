from flask import Flask
from backend.controllers import catalogs_app, items_app, users_app
from backend.api_controllers import catalogs_api_app, items_api_app
from backend.config import create_schema, connect, generate_csrf_token
from backend.models import Catalog, Item, User


app = Flask(__name__, template_folder='frontend/templates', static_folder='frontend')
app.jinja_env.globals['csrf_token'] = generate_csrf_token

app.register_blueprint(catalogs_app)
app.register_blueprint(items_app)
app.register_blueprint(users_app)

app.register_blueprint(catalogs_api_app)
app.register_blueprint(items_api_app)

create_schema()

@app.route("/")
def root():
    return "Hello World!"



if __name__ == "__main__":
    app.run(port=8080, host='0.0.0.0', debug=True)
