from rest_framework import generics
from personal.models import User
from personal.serializers import UserSerializer


class UserView(generics.ListCreateAPIView):
    """
    Returns a list of all users.
    """
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserInstanceView(generics.RetrieveUpdateDestroyAPIView):
    """
    Returns a single user.
    Also allows updating and deleting.
    """
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
