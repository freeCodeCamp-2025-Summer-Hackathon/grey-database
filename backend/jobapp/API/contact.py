from datetime import datetime, timezone

from flask import Blueprint, request, session
from jobapp.models import  Application, Contact
bp = Blueprint('Contact', __name__)

@bp.route("/<string:application_id>/contacts/create", methods=["POST"])
def create_contact(application_id):
    """
    API to create a contact for an application
    ---
    tags:
      - Contacts
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
            - name
            - email
          properties:
            name:
              type: string
            email:
              type: string
    responses:
      201:
        description: Contact created successfully
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
    data = request.get_json()
    if not data or not data.get("name") or not data.get("email"):
        return {'error': 'Data not valid'}, 400

    application = Application.objects(id=application_id).first()
    if not application:
        return {'error': 'Application not found'}, 400

    contact = Contact(
        name=data["name"],
        email=data["email"]
    )
    application.contacts.append(contact)
    application.save()
    return {"message": "Contact created successfully", "index": len(application.contacts) - 1}, 201

@bp.route("/<string:application_id>/contacts/<int:index>", methods=["GET"])
def get_contact(application_id, index):
    """
    API to retrieve a contact by index in an application
    ---
    tags:
      - Contacts
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
        description: Contact found
        schema:
          type: object
          properties:
            name:
              type: string
            email:
              type: string
      404:
        description: Contact or application not found
    """
    application = Application.objects(id=application_id).first()
    if not application or index < 0 or index >= len(application.contacts):
        return {'error': 'Contact not found'}, 404

    contact = application.contacts[index]

    return {
        "name": contact.name,
        "email": contact.email,
    }, 200

@bp.route("/<string:application_id>/contacts/<int:index>", methods=["PATCH"])
def edit_contact(application_id, index):
    """
    API to update a contact by index in an application
    ---
    tags:
      - Contacts
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
            name:
              type: string
            email:
              type: string
    responses:
      200:
        description: Contact updated successfully
      404:
        description: Contact or application not found
    """
    data = request.get_json()
    application = Application.objects(id=application_id).first()
    if not application or index < 0 or index >= len(application.contacts):
        return {'error': 'Contact not found'}, 404

    if "name" in data:
        application.contacts[index]["name"] = data["name"]
    if "email" in data:
        application.contacts[index]["email"] = data["email"]
    application.save()
    return {"message": "Contact updated successfully"}, 200


@bp.route("/contacts/<string:application_id>/<int:index>", methods=["DELETE"])
def delete_contact(application_id, index):
    """
    API to delete a contact by index in an application
    ---
    tags:
      - Contacts
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
        description: Contact deleted successfully
      404:
        description: Contact or application not found
    """
    application = Application.objects(id=application_id).first()
    if not application or index < 0 or index >= len(application.contacts):
        return {'error': 'Contact not found'}, 404

    del application.contacts[index]
    application.save()
    return {"message": "Contact deleted successfully"}, 200
