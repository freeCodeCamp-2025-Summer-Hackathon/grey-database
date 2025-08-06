from datetime import datetime, timezone

from flask import Blueprint, request, session
from jobapp.models import User, Application, Note, StatusEnum

bp = Blueprint('Note', __name__)

@bp.route("/<string:application_id>/notes/create", methods=["POST"])
def add_note(application_id):
    """
    API to add a note to a specific application
    ---
    tags:
      - Notes
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
            - note
            - status
          properties:
            note:
              type: string
              example: "Called the candidate"
            status:
              type: string
              enum: [OPEN, CLOSED]
              example: "OPEN"
    responses:
      201:
        description: Note added successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: Note added successfully
      400:
        description: Invalid input
        schema:
          type: object
          properties:
            error:
              type: string
      404:
        description: Application not found
        schema:
          type: object
          properties:
            error:
              type: string
    """
    data = request.get_json()
    try:
        note = Note(
            note=data["note"],
            added=datetime.now(timezone.utc),
            status=StatusEnum(data["status"])
        )
        app_doc = Application.objects(id=application_id).first()
        if not app_doc:
            return {"error": "Application not found"}, 404

        app_doc.notes.append(note)
        app_doc.save()
        return {"message": "Note added successfully"}, 201
    except Exception as e:
        return {"error": str(e)}, 400


@bp.route("/<string:application_id>/notes", methods=["GET"])
def get_notes(application_id):
    """
    API to retrieve all notes for a specific application
    ---
    tags:
      - Notes
    parameters:
      - name: application_id
        in: path
        type: string
        required: true
        description: ID of the application
    responses:
      200:
        description: List of notes
        schema:
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
    """
    app_doc = Application.objects(id=application_id).first()
    if not app_doc:
        return {"error": "Application not found"}, 404
    return [{
        "note": n.note,
        "added": n.added.isoformat(),
        "status": n.status.value
    } for n in app_doc.notes], 200


@bp.route("/<string:application_id>/notes/<int:index>", methods=["PATCH"])
def edit_note(application_id, index):
    """
    API to update a note in a specific application by index
    ---
    tags:
      - Notes
    parameters:
      - name: application_id
        in: path
        type: string
        required: true
        description: ID of the application
      - name: index
        in: path
        type: integer
        required: true
        description: Index of the note in the notes array
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            note:
              type: string
              example: "Updated note content"
            status:
              type: string
              enum: [OPEN, CLOSED]
              example: "CLOSED"
    responses:
      200:
        description: Note updated successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: Note updated successfully
      404:
        description: Application or note not found
        schema:
          type: object
          properties:
            error:
              type: string
    """
    data = request.get_json()
    app_doc = Application.objects(id=application_id).first()
    if not app_doc:
        return {'error': 'Application not found'}, 404

    if index < 0 or index >= len(app_doc.notes):
        return {'error': 'Note not found'}, 404

    note = app_doc.notes[index]
    note.note = data.get("note", note.note)
    if "status" in data:
        note.status = StatusEnum(data["status"])
    app_doc.save()
    return {'message': 'Note updated successfully'}, 200


@bp.route("/<string:application_id>/notes/<int:index>", methods=["DELETE"])
def delete_note(application_id, index):
    """
    API to delete a note from a specific application by index
    ---
    tags:
      - Notes
    parameters:
      - name: application_id
        in: path
        type: string
        required: true
        description: ID of the application
      - name: index
        in: path
        type: integer
        required: true
        description: Index of the note in the notes array
    responses:
      200:
        description: Note deleted successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: Note deleted successfully
      404:
        description: Application or note not found
        schema:
          type: object
          properties:
            error:
              type: string
    """
    app_doc = Application.objects(id=application_id).first()
    if not app_doc:
        return {'error': 'Application not found'}, 404

    if index < 0 or index >= len(app_doc.notes):
        return {'error': 'Note not found'}, 404

    del app_doc.notes[index]
    app_doc.save()
    return {'message': 'Note deleted successfully'}, 200
