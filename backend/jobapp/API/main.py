from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route("/", methods=['GET'])
def hello():
    """
    App bootup.
    ---
    responses:
      200:
        description: Job Application online
      401:
        description: Unauthorized
    """
    return "Job Application online"