from django.db.models import QuerySet
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.request import Request
from apps.login.models import CustomUser
from apps.character.serializers import *
from apps.character.models import *


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all().order_by('id')
    serializer_class = CharacterSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    http_method_names = ['get', 'post', 'put', 'delete']

    def list(self, request: Request, *args, **kwargs) -> Response:
        try:
            user: CustomUser = CustomUser.objects.get(user=request.user)
            queryset: QuerySet[Character, Character] = self.queryset.filter(user=user)

            if user.level == 0:
                return Response(CharacterSerializer(self.queryset, many=True).data, status=status.HTTP_200_OK)

            serializer: CharacterSerializer = CharacterSerializer(queryset, many=True)

            if not serializer.data:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'errors': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request: Request, *args, **kwargs) -> Response:
        try:
            user: CustomUser = CustomUser.objects.get(user=request.user)
            instance = self.get_object()

            character_owner: CustomUser = instance.user

            if character_owner != user and user.level != 0:
                    return Response(status=status.HTTP_403_FORBIDDEN)

            response = {
                'name': instance.name,
                'age': instance.age,
                'description': instance.description,
                'attributes': model_to_dict(instance.attributes, fields=[
                    'strength', 'dexterity', 'intelligence', 'presence', 'vigor'
                ]) if instance.attributes else None,
                'skills': model_to_dict(instance.skills, exclude=['character', 'id']) if instance.skills else None,
            }

            return Response(response, status=status.HTTP_200_OK)

        except Character.DoesNotExist:
            return Response({'error': 'Character not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AttributesViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Attributes, Attributes] = Attributes.objects.all().order_by('id')
    serializer_class: AttributesSerializer = AttributesSerializer
    http_method_names: list[str] = ['get', 'post', 'put', 'delete']


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all().order_by('id')
    serializer_class = SkillSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        character_id = data.pop('character')

        character = Character.objects.get(id=character_id)

        if not character:
            return Response({'error': 'Character not found'}, status=status.HTTP_404_NOT_FOUND)

        for field in data:
            levels = {
                'U': 0,
                'T': 5,
                'V': 10,
                'E': 15,
            }

            data[field]['total'] = levels[data[field]
                                          ['level']] + data[field]['bonus']

            print(data[field])

        data['character'] = character_id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class OriginViewSet(viewsets.ModelViewSet):
    queryset = Origin.objects.all().order_by('id')
    serializer_class = OriginSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all().order_by('id')
    serializer_class = ClassSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class SubclassViewSet(viewsets.ModelViewSet):
    queryset = Subclass.objects.all().order_by('id')
    serializer_class = SubclassSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all().order_by('id')
    serializer_class = InventorySerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class AvailableAbilitiesViewSet(viewsets.ModelViewSet):
    queryset = AvailableAbilities.objects.all().order_by('id')
    serializer_class = AvailableAbilitiesSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class AvailableRitualsViewSet(viewsets.ModelViewSet):
    queryset = AvailableRituals.objects.all().order_by('id')
    serializer_class = AvailableRitualsSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class AvailableParanormalPowersViewSet(viewsets.ModelViewSet):

    queryset = AvailableParanormalPowers.objects.all().order_by('id')
    serializer_class = AvailableParanormalPowersSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class ClassProgressionViewSet(viewsets.ModelViewSet):
    queryset = ClassProgression.objects.all().order_by('id')
    serializer_class = ClassProgressionSerializer
    http_method_names = ['get', 'post', 'put', 'delete']