from rest_framework import serializers
from personal.models import User, UserDetail


class UserSerializer(serializers.ModelSerializer):
    """
    Serialize all the users.
    """

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
