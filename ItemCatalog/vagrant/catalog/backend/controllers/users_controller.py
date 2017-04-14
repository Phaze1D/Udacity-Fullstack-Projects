from flask import Blueprint, render_template, abort, request
from apiclient import discovery
import httplib2
from oauth2client import client

import logging

users_app = Blueprint('users', __name__)


@users_app.route('/google-signin',  methods=['POST'])
def google_signin():
    if not request.headers.get('X-Requested-With'):
        abort(403)


    credentials = client.credentials_from_clientsecrets_and_code(
    'backend/config/google_data.json',
    ['profile', 'email'],
    request.data)

    logging.warning( credentials.id_token['email'])

    return 'oooooo'


@users_app.route('/oauth2callback')
def google_callback(arg):

    return 'sdaf';
