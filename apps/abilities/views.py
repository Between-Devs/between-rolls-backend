from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework import viewsets, status
from apps.abilities.serializers import *
from apps.abilities.models import *


class AbilityViewSet(viewsets.ModelViewSet):
    queryset = Ability.objects.all().order_by('id')
    serializer_class = AbilitySerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class RitualsViewSet(viewsets.ModelViewSet):
    queryset = Rituals.objects.all().order_by('id')
    serializer_class = RitualsSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class ParanormalPowersViewSet(viewsets.ModelViewSet):
    queryset = ParanormalPowers.objects.all().order_by('id')
    serializer_class = ParanormalPowersSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
