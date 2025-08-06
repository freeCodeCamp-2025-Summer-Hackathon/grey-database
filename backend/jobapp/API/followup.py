from datetime import datetime, timezone

from flask import Blueprint, request, session
from jobapp.models import User, Application, Followup

bp = Blueprint("Followup", __name__)


@bp.route("/<string:application_id>/followups/create", methods=["POST"])
def create_followup(application_id):
    """
    API to create a followup for an application
    ---
    tags:
      - Followups
    consumes:
      - application/json
    parameters:
      - name: application_id
        in: path
        type: string
        required: true
        description: ID of the application
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - date
          properties:
            date:
              type: string
              format: date-time
              example: "2025-07-22T10:00:00Z"
    responses:
      201:
        description: Followup created successfully
        schema:
          type: object
          properties:
            message:
              type: string
            index:
              type: integer
      400:
        description: Invalid input
    """
    from datetime import datetime

    data = request.get_json()
    if not data or not data.get("date"):
        return {"error": "Data not valid"}, 400

    application = Application.objects(id=application_id).first()
    if not application:
        return {"error": "Application not found"}, 400

    try:
        parsed_date = datetime.fromisoformat(data["date"].replace("Z", "+00:00"))
    except Exception:
        return {"error": "Invalid date format"}, 400

    followup = Followup(
        date=parsed_date
    )
    application.followups.append(followup)
    application.save()
    return {
        "message": "Followup created successfully",
        "index": len(application.followups) - 1,
    }, 201


@bp.route("/<string:application_id>/followups/<int:index>", methods=["GET"])
def get_followup(application_id, index):
    """
    API to retrieve a followup by index in an application
    ---
    tags:
      - Followups
    parameters:
      - name: application_id
        in: path
        type: string
        required: true
      - name: index
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Followup found
        schema:
          type: object
          properties:
            date:
              type: string
              format: date-time
      404:
        description: Followup or application not found
    """
    application = Application.objects(id=application_id).first()
    if not application or index < 0 or index >= len(application.followups):
        return {"error": "Followup not found"}, 404

    followup = application.followups[index]
    return {"date": followup["date"].isoformat()}, 200


@bp.route("/<string:application_id>/followups/<int:index>", methods=["PATCH"])
def edit_followup(application_id, index):
    """
    API to update a followup by index in an application
    ---
    tags:
      - Followups
    parameters:
      - name: application_id
        in: path
        type: string
        required: true
      - name: index
        in: path
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            date:
              type: string
              format: date-time
              example: "2025-07-23T15:00:00Z"
    responses:
      200:
        description: Followup updated successfully
      404:
        description: Followup or application not found
    """
    from datetime import datetime

    data = request.get_json()
    application = Application.objects(id=application_id).first()
    if not application or index < 0 or index >= len(application.followups):
        return {"error": "Followup not found"}, 404

    if "date" in data:
        try:
            application.followups[index]["date"] = datetime.fromisoformat(
                data["date"].replace("Z", "+00:00")
            )
        except Exception:
            return {"error": "Invalid date format"}, 400

    application.save()
    return {"message": "Followup updated successfully"}, 200


@bp.route("/<string:application_id>/followups/<int:index>", methods=["DELETE"])
def delete_followup(application_id, index):
    """
    API to delete a followup by index in an application
    ---
    tags:
      - Followups
    parameters:
      - name: application_id
        in: path
        type: string
        required: true
      - name: index
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Followup deleted successfully
      404:
        description: Followup or application not found
    """
    application = Application.objects(id=application_id).first()
    if not application or index < 0 or index >= len(application.followups):
        return {"error": "Followup not found"}, 404

    del application.followups[index]
    application.save()
    return {"message": "Followup deleted successfully"}, 200
