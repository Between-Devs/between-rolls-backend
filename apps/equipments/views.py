from rest_framework import viewsets, status
from apps.equipments.serializer import *
from apps.equipments.models import *


class WeaponViewSet(viewsets.ModelViewSet):
    queryset = Weapon.objects.all().order_by('id')
    serializer_class = WeaponSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


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
