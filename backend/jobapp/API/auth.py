from flask import Blueprint, request, session
from jobapp.models import User

bp = Blueprint('UserAuth', __name__)

@bp.route("/register", methods=['post'])
def register():
    """
    API to register a new user
    ---
    tags:
      - Auth
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - username
            - password
          properties:
            username:
              type: string
              example: johndoe
            password:
              type: string
              example: secret123
    responses:
      201:
        description: User registered successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: User registered successfully
            userid:
              type: string
              description: ID of the newly registered user
      400:
        description: Username and password required
        schema:
          type: object
          properties:
            error:
              type: string
              example: Username and password required
      409:
        description: Username already exists
        schema:
          type: object
          properties:
            error:
              type: string
              example: Username already exists
    """
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return {'error': 'Username and password required'}, 400
    
    if User.objects(username=data['username']):
        return {'error': 'Username already exists'}, 409

    user = User(username=data['username'], password=data['password'])
    user.save()
    return {'message': 'User registered successfully', 'userid': str(user.id)}, 201

@bp.route("/login", methods=["POST",])
def login():
    """
    API to log in a registered user
    ---
    tags:
      - Auth
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - username
            - password
          properties:
            username:
              type: string
              example: johndoe
            password:
              type: string
              example: secret123
    responses:
      200:
        description: Logged in successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: Logged in successfully
            userid:
              type: string
              description: ID of the logged-in user
      401:
        description: Invalid credentials
    """
    data = request.get_json()
    user = User.objects(username=data.get('username'), password=data.get('password')).first()
    if user:
        session['username'] = user.username
        return {'message': 'Logged in successfully', 'userid': user.id}, 200
    return {'error': 'Invalid credentials'}, 401