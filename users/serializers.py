from rest_framework import serializers

from users.models import User


class PrivateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'password',
        )
