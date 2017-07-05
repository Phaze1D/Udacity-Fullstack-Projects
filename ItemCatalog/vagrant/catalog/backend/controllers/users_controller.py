from flask import Blueprint, render_template, request, jsonify, session
from apiclient import discovery
from oauth2client import client
from backend.models import User
from backend.helpers import login, check_csrf, generate_csrf_token
import httplib2


users_app = Blueprint('users', __name__)


@users_app.route('/googlesignin',  methods=['POST'])
@check_csrf
def google_signin():
    """Function that logs in a user and adds there info to the database
    if the haven't already been added.

    Returns:
        Newly created csrf_token
    """
    credentials = client.credentials_from_clientsecrets_and_code(
        './backend/config/google.json',
        ['profile', 'email'],
        request.form.get('code'))

    user = User.find_by_email(credentials.id_token['email'])
    if user == None:
        user = User.create(credentials.id_token['email'])
    login(user)

    return jsonify(csrf_token = generate_csrf_token())


@users_app.route('/logout', methods=['POST'])
@check_csrf
def logout():
    """Function that removes a user's id from the session causing them to
    be logout

    Returns:
        Newly created csrf_token
    """
    session.pop('user', None)
    return jsonify(csrf_token = generate_csrf_token())
