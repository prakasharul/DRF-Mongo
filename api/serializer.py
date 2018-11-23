from rest_framework_mongoengine.serializers import EmbeddedDocumentSerializer, DocumentSerializer
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from . validatators import FieldValidators
import re

from . models import User, UserDetails


class UserDetailsSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = UserDetails


class UserSerializer(DocumentSerializer):
    email = serializers.EmailField()
    userdetails = UserDetailsSerializer

    class Meta:
        model = User
        depth = 2
        fields = '__all__'

    def validate(self, attrs):
        self.error = {}
        userdetails = dict(attrs['userdetails'][0])
        if not re.match('^[0-9]*$', str(userdetails['pincode'])):
            self.error["pincode"] = "invalid pincode"

        if not re.match('[a-zA-Z0-9\_\-\.]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$', attrs['email']):
            self.error["email"] = "invalid email"

        if not re.match('^[a-zA-Z]*$', attrs['username']):
            self.error["username"] = "invalid username"

        if not re.match('^[a-zA-Z]*$', attrs['firstname']):
            self.error["firstname"] = "firstname invalid"

        if self.error:
            print(self.error)
            raise serializers.ValidationError(self.error)

        return  attrs


    # def validate_pincode(self, pincode):
    #     if not re.match('^[0-9]*$', pincode):
    #         raise serializers.ValidationError('pincode invalid')
    #     return pincode
    #
    # def validate_firstname(self, firstname):
    #     if not re.match('^[a-zA-Z]*$', firstname):
    #         raise serializers.ValidationError('firstname should be alpha')
    #     return firstname
    # def validate_email(self, email):
    #     if not re.match('[a-zA-Z0-9\_\-\.]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$', email):
    #         raise serializers.ValidationError('email is invalid')
    #     return email
    #
    # def validate_username(self, username):
    #     if not re.match('^[a-zA-Z]*$', username):
    #         raise serializers.ValidationError('username should contains only aplha')
    #     return username

    def update(self, instance, validated_data):
        email = validated_data.pop("email")
        updated_instance = super().update(instance, validated_data)
        return updated_instance


