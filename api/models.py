from mongoengine import  Document, fields, EmbeddedDocument, ListField, EmbeddedDocumentField



class UserDetails(EmbeddedDocument):
    address1 = fields.StringField(required=True, max_length=200)
    address2 = fields.StringField(required=False, max_length=200)
    state    = fields.StringField(required=True)
    country  = fields.StringField(required=True)
    pincode  = fields.IntField(required=True)

class User(Document):

    username = fields.StringField(required=True)
    email    = fields.EmailField(required = True, )
    firstname= fields.StringField(required= True)
    lastname = fields.StringField(required=True, null=True)
    status   = fields.IntField(required=True, default=1)
    userdetails  = ListField(EmbeddedDocumentField('UserDetails'))

