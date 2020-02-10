# api/serializers.py
from rest_framework import serializers
from sss import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'email',
            'password',


        )
        model = models.User


