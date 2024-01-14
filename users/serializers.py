from rest_framework import serializers

from users.models import User


class PrivateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'password',
            'is_superuser',
            'id',
            'is_staff',
            'is_active',
            'first_name',
            'last_name',
            'groups',
            'user_permissions'
        )
