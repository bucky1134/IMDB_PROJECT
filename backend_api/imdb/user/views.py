from  django.contrib.auth.models import User
from rest_framework.response  import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from .serializers import UserRegisterSerializer
from rest_framework.authtoken.models import Token

#created function based view with no permission so that any user can register

@api_view(['POST'])
@permission_classes([AllowAny])
def UserRegister(requests):
    serialized = UserRegisterSerializer(data=requests.data)
    #saving instance to db when there is valid serialization else throwing error response
    if serialized.is_valid():
        serialized.save()
        user=User.objects.get(username=serialized.data['username'])
        token = Token.objects.create(user=user)
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

