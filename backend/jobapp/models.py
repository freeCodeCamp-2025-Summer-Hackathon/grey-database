from mongoengine import (
    Document, EmbeddedDocument,
    StringField, ReferenceField, ListField,
    DateTimeField, EnumField, EmbeddedDocumentField,
    FileField, IntField
)
import enum

class StatusEnum(enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"

class User(Document):
    username = StringField(required=True)
    password = StringField()

class Note(EmbeddedDocument):
    note = StringField(required=True)
    added = DateTimeField(required=True)
    status = EnumField(StatusEnum, required=True)

class Application(Document):
    userid = ReferenceField(User, required=True, reverse_delete_rule=2)
    name = StringField(required=True)
    notes = ListField(EmbeddedDocumentField(Note))

class Contact(Document):
    applicationid = ReferenceField(Application, required=True, reverse_delete_rule=2)
    name = StringField(required=True)
    email = StringField(required=True)  

class Followup(Document):
    applicationid = ReferenceField(Application, required=True, reverse_delete_rule=2)
    date = DateTimeField(required=True)

