from flask import Blueprint, request, session
from jobapp.models import User, Application

bp = Blueprint('Application', __name__)

@bp.route("/create", methods=['POST'])
def create_application():
    """
    API to create a new job application for a user
    ---
    tags:
      - Applications
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - userid
            - name
          properties:
            userid:
              type: string
              example: "64f1a2e7c6d0fdb2c1f6a1b2"
            name:
              type: string
              example: "Software Engineer at Google"
    responses:
      201:
        description: Application created successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: Application created successfully
            id:
              type: string
              description: ID of the created application
      400:
        description: Invalid input or user does not exist
        schema:
          type: object
          properties:
            error:
              type: string
              example: Data not valid
      500:
        description: Internal server error
    """
    try:
        data = request.get_json()
        if not data or not data.get("userid") or not data.get("name"):
            return {'error': 'Data not valid'}, 400

        user = User.objects(id=data["userid"]).first()
        if not user:
            return {'error': 'User does not exist'}, 400

        application = Application(userid=user, name=data["name"])
        application.save()

        return {'message': 'Application created successfully', 'id': str(application.id)}, 201

    except Exception as e:
        # Optionally log the error
        print("Error:", e)
        return {'error': 'Internal server error'}, 500

@bp.route("/<string:id>", methods=['GET'])
def get_application(id):
    """
    API to retrieve a job application by ID
    ---
    tags:
      - Applications
    parameters:
      - name: id
        in: path
        type: string
        required: true
        description: ID of the application to retrieve
    responses:
      200:
        description: Application found
        schema:
          type: object
          properties:
            message:
              type: string
              example: Application found
            id:
              type: string
            name:
              type: string
            userid:
              type: string
            notes:
              type: array
              items:
                type: object
                properties:
                  note:
                    type: string
                  added:
                    type: string
                    format: date-time
                  status:
                    type: string
      404:
        description: Application not found
        schema:
          type: object
          properties:
            error:
              type: string
              example: Application not found
    """
    application = Application.objects(id=id).first()
    if not application:
        return {'error': 'Application not found'}, 404

    return {
        'message': 'Application found',
        'id': str(application.id),
        'name': application.name,
        'userid': str(application.userid.id),
        'notes': [
            {
                'note': note.note,
                'added': note.added.isoformat(),
                'status': note.status.value
            }
            for note in application.notes
        ]
    }, 200

    
@bp.route("/user-applications", methods=['POST'])
def user_applications():
    """
    API to fetch all job applications for a specific user
    ---
    tags:
      - Applications
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - userid
          properties:
            userid:
              type: string
              description: ID of the user
              example: "64f1a2e7c6d0fdb2c1f6a1b2"
    responses:
      200:
        description: Applications found
        schema:
          type: object
          properties:
            message:
              type: string
              example: Applications found
            applications:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: string
                  name:
                    type: string
                  userid:
                    type: string
                  notes:
                    type: array
                    items:
                      type: object
                      properties:
                        note:
                          type: string
                        added:
                          type: string
                          format: date-time
                        status:
                          type: string
      400:
        description: Invalid input
        schema:
          type: object
          properties:
            error:
              type: string
              example: Data not valid
    """
    data = request.get_json()
    if not data or not data.get("userid"):
        return {'error': 'Data not valid'}, 400

    applications = Application.objects(userid=data.get("userid")).all()

    serialized_apps = []
    for app in applications:
        serialized_apps.append({
            'id': str(app.id),
            'name': app.name,
            'userid': str(app.userid.id),
            'notes': [
                {
                    'note': note.note,
                    'added': note.added.isoformat(),
                    'status': note.status.value
                }
                for note in app.notes
            ]
        })

    return {'message': 'Applications found', 'applications': serialized_apps}, 200

@bp.route("/<string:id>", methods=['PATCH'])
def edit_application(id):
    """
    API to update a job application by ID
    ---
    tags:
      - Applications
    parameters:
      - name: id
        in: path
        type: string
        required: true
        description: ID of the application to update
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: New name of the application
    responses:
      200:
        description: Application updated successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: Application updated successfully
      400:
        description: Invalid input
        schema:
          type: object
          properties:
            error:
              type: string
              example: Data not valid
      404:
        description: Application not found
    """
    data = request.get_json()
    application = Application.objects(id=id).first()
    if not application:
        return {'error': 'Application not found'}, 404

    if not data or not data.get("name"):
        return {'error': 'Data not valid'}, 400

    application.name = data["name"]
    application.save()
    return {'message': 'Application updated successfully'}, 200


@bp.route("/<string:id>", methods=['DELETE'])
def delete_application(id):
    """
    API to delete a job application by ID
    ---
    tags:
      - Applications
    parameters:
      - name: id
        in: path
        type: string
        required: true
        description: ID of the application to delete
    responses:
      200:
        description: Application deleted successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: Application deleted successfully
      404:
        description: Application not found
        schema:
          type: object
          properties:
            error:
              type: string
              example: Application not found
    """
    application = Application.objects(id=id).first()
    if not application:
        return {'error': 'Application not found'}, 404

    application.delete()
    return {'message': 'Application deleted successfully'}, 200