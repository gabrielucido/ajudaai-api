import re
from unidecode import unidecode

from rest_framework import viewsets, status
from rest_framework.response import Response
from users.models import User
from random import randint
from rest_framework.authtoken.models import Token

from users.serializers import CreateAnonUserSerializer
import secrets
import string


class CreateAnonUser(viewsets.GenericViewSet, viewsets.mixins.CreateModelMixin):
    """
    Create anon user and return id and auth token.
    """
    queryset = User.objects.all()
    serializer_class = CreateAnonUserSerializer

    def create(self, request, *args, **kwargs):
        """
        Create anon user and return id and auth token.
        """
        name = request.data.get('name', False)
        #generate a random password with length of 16 with alphanumeric characters
        if name:
            username = unidecode(re.sub(' +', '-', name.strip()))
            password = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(16))
            #while username already exists, generate a new with username + random number
            while User.objects.filter(username=username).exists():
                username = username + str(randint(0, 9))
            user = User.objects.create_user(username=username, password=password)
            user.token = Token.objects.get_or_create(user=user)[0]
            return Response(CreateAnonUserSerializer(user).data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
