from functools import wraps
from flask import request, jsonify

from homework_api import app

from homework_api.models import User

import jwt

# Creating a custom decorator to validate the API KEY
# that is passed in to a specific route

def token_required(our_flask_function):
    # Copy the contents of the return function, most specifically
    # we are gathering parameters from the returned function. 
    @wraps(our_flask_function)
    def decorated(*args, **kwargs):
        token = None

        try:
            if 'x-access-token' in request.headers:
                token = request.headers['x-access-token'].split(" ")[1]
        except:
            if not token:
                return jsonify({'message': 'Token is missing!!'}), 401
        try:
            data = jwt.decode(token,app.config['SECRET_KEY'])
            current_user_token = User.query.filter_by(id = data['public_id']).first()
        except:
            data = jwt.decode(token,app.config['SECRET_KEY'])
            return jsonify({'message': 'Token is invalid'}), 401
        return our_flask_function(current_user_token,*args,**kwargs)

    return decorated