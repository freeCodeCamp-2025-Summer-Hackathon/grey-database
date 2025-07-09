from flask import Blueprint, request
from jobapp.models import User

bp = Blueprint('UserAuth', __name__)

@bp.route("/register", methods=['post'])
def registerUser():
    """
    API to register user for the app
    ---
    tags:
      - Auth
    parameters:
      - name: username
        in: formData
        type: string
        required: false
      - name: password
        in: formData
        type: string
        required: false
    responses:
      200:
        description: Registered successfully
      401:
        description: Unauthorized
    """
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return {'error': 'Username and password required'}, 400
    
    if User.objects(username=data['username']):
        return {'error': 'Username already exists'}, 400

    user = User(username=data['username'], password=data['password'])
    user.save()
    return {'message': 'User registered successfully'}, 201

@bp.route("/login")
def loginUser():
    return "User logged in"

@bp.route("/reset")
def resetUserCredtentials():
    return "User registered"