from flask import Blueprint
from jobapp.Models.User import User

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
    user = User()
    user.username = 'grey_test1@yopmail.com'
    user.password = 'greypass1'
    user.save()
    return "User registered"

@bp.route("/login")
def loginUser():
    return "User logged in"

@bp.route("/reset")
def resetUserCredtentials():
    return "User registered"