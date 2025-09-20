from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from drf_yasg import openapi
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
        """
        Listagem de todos os Usuários cadastrados no sistema.
        **Disponível apenas para Admins.**
        """
        try:
            serializer: UserSerializer = UserSerializer(
                self.queryset, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs) -> Response:
        """
        Retorna os dados de um *User* especificado.
        **Disponível apenas para Admins.**
        """
        try:
            instance: CustomUser = self.get_object()

            data = {
                'username': instance.user.username,
                'level': instance.level
            }

            return Response(data, status=status.HTTP_200_OK)

        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        """
        Cria a atribuição de um *User* existente com um novo *CustomUser*.
        **Disponível apenas para Admins.**
        """
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Atualiza os dados de um *CustomUSer* especificado.
        **Disponível apenas para Admins.**
        """
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Deleta o *CustomUser* e seu *User* atrelado.
        **Disponível apenas para Admins.**
        """

        user: CustomUser = self.get_object()
        user.user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='username'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='password'),
        },
        required=['username', 'password'],
        example={
            "username": "testuser",
            "password": "testpassword"
        }
    ),
    responses={
        200: openapi.Response(
            description="Login successful",
            examples={
                "application/json": {
                    "username": "testuser",
                    "level": 1,
                    "token": "your-auth-token"
                }
            }
        ),
        400: openapi.Response(
            description="Username and password are required",
            examples={
                "application/json": {
                    "error": "Username and password are required"
                }
            }
        ),
        401: openapi.Response(
            description="Invalid credentials",
            examples={
                "application/json": {
                    "error": "Invalid credentials"
                }
            }
        ),
        404: openapi.Response(
            description="User not found",
            examples={
                "application/json": {
                    "error": "User not found"
                }
            }
        )
    }
)
@api_view(['POST'])
def login(request) -> Response:
    """
    Permite o login do *User*.
    """
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


@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='username'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='password'),
        },
        required=['username', 'password'],
        examples={
            "username": "testuser",
            "password": "testpassword"
        }
    ),
    responses={
        201: openapi.Response(
            description="Created successful",
            examples={
                "application/json": {
                    "username": "testuser",
                }
            }
        ),
        400: openapi.Response(
            description="Username and password are required, or username already exists.",
            examples={
                "application/json": {
                    "error": "message"
                },
            }
        )
    }
)
@api_view(['POST'])
def signup(request) -> Response:
    """
    Permite o cadastro de um novo usuário.
    """
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user: User = User.objects.create_user(username, password)
        user.save()

        custom_user: CustomUser = CustomUser.objects.create(user=user, level=1)
        custom_user.save()

        return Response({'user': user.username}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)