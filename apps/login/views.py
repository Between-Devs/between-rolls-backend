from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from .permissions import *
from .serializers import *
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = [IsAdminUser]
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request, *args, **kwargs):
        try:
            serializer: UserSerializer = UserSerializer(
                self.queryset, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs) -> Response:
        try:
            instance: CustomUser = self.get_object()
            token, created = Token.objects.get_or_create(user=instance.user)
            data = {
                'username': instance.user.username,
                'level': instance.level,
                'token': token.key
            }
            return Response(data, status=status.HTTP_200_OK)

        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def login(request) -> Response:
    print(request)
    print(request.data)
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = CustomUser.objects.get(user__username=username)
        if user.user.check_password(password):
            token, created = Token.objects.get_or_create(user=user.user)
            data = {
                'username': user.user.username,
                'level': user.level,
                'token': token.key
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    except CustomUser.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
