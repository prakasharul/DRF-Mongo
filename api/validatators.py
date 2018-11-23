import re
from rest_framework import serializers


class FieldValidators():

    def username(self, value):
            if value.isalpha():
                return value
            else:
                raise serializers.ValidationError('username should contain alpha')

