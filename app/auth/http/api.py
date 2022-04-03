from datetime import datetime, timedelta
from http import HTTPStatus

from flask import Blueprint, request, make_response, current_app, jsonify
from werkzeug.security import check_password_hash

from app.errors import bad_request, internal_server
from app.logger import log_error
from app.repository.user_repository import UserRepository

import jwt

auth = Blueprint('auth', __name__)

user_repository = UserRepository()


@auth.route("/register", methods=["POST"])
def register():
    try:
        data = request.json
        username = data['username']
        email = data['email']
        password = data['password']

        response_dict = user_repository.add(username, email, password)
        id_user = response_dict['uuid']
        return response_dict, HTTPStatus.CREATED, {'location': f'/user/{id_user}'}
    except KeyError as e:
        log_error(e)
        return bad_request()
    except Exception as e:
        log_error(e)
        return internal_server(e)


@auth.route('/login', methods=['POST'])
def login():
    try:
        # creates dictionary of form data
        data = request.json
        username = data['username']
        password = data['password']

        if not username or not password:
            # returns 401 if any email or / and password is missing
            return make_response(
                'Could not verify',
                401,
                {'WWW-Authenticate': 'Basic realm ="Login required !!"'}
            )

        user = user_repository.get(username)

        if not user:
            # returns 401 if user does not exist
            return make_response(
                'Could not verify',
                401,
                {'WWW-Authenticate': 'Basic realm ="Login required !!"'}
            )

        if check_password_hash(user.password_hash, password):
            public_id: str = str(user.uuid)
            exp: str = str(datetime.utcnow() + timedelta(minutes=30))
            private_key = current_app.config['SECRET_KEY'][0]
            nl = '\n'
            format_key: str = '-----BEGIN PUBLIC KEY-----\n' + private_key + '\n-----END PUBLIC KEY-----'
            algorithm: str = "RS256"


            # generates the JWT Token
            token = jwt.encode(payload={'public_id': public_id, 'exp': exp}, key=format_key, algorithm=algorithm)

            return jsonify({'token': token.decode('UTF-8')}), 201
        # returns 403 if password is wrong
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm ="Login required !!"'}
        )
    except KeyError as e:
        log_error(e)
        return bad_request()
    except Exception as e:
        log_error(e)
        return internal_server(e)
