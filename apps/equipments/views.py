from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from apps.login.permissions import IsAdminUser
from rest_framework import viewsets, filters
from .filters import WeaponFilter
from .serializer import *
from .models import *


class WeaponViewSet(viewsets.ModelViewSet):
    queryset = Weapon.objects.all().order_by('id')
    serializer_class = WeaponSerializer

    authentication_classes = (SessionAuthentication, TokenAuthentication)

    http_method_names = ['get', 'post', 'put', 'delete']

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['weapon_name']
    filterset_class = WeaponFilter

    def get_permissions(self):
        if self.action != "retrive" and self.action != "list":
            return [IsAdminUser()]
        
        return [IsAuthenticated()]


class WeaponModViewSet(viewsets.ModelViewSet):
    queryset = WeponMods.objects.all().order_by('id')
    serializer_class = WeaponModSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class AmmoViewSet(viewsets.ModelViewSet):

    queryset = Ammo.objects.all().order_by('id')
    serializer_class = AmmoSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class ArmorViewSet(viewsets.ModelViewSet):
    queryset = Armor.objects.all().order_by('id')
    serializer_class = ArmorSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class ArmorModViewSet(viewsets.ModelViewSet):
    queryset = ArmorMod.objects.all().order_by('id')
    serializer_class = ArmorModSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class GeneralEquipmentViewSet(viewsets.ModelViewSet):
    queryset = GeneralEquipment.objects.all().order_by('id')
    serializer_class = GeneralEquipmentSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class AccessoriesModViewSet(viewsets.ModelViewSet):
    queryset = AccessoriesMod.objects.all().order_by('id')
    serializer_class = AccessoriesModSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class ParanormalItensViewSet(viewsets.ModelViewSet):
    queryset = ParanormalItens.objects.all().order_by('id')
    serializer_class = ParanormalItensSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
