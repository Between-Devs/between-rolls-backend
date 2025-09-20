from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from apps.login.permissions import IsAdminUser
from rest_framework import viewsets, filters
from .filters import WeaponFilter, WeaponModFilter
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

    def list(self, request, *args, **kwargs):
        """
        Lista todas as Armas, cadastradas do sistema (Ordem Paranormal).
        """
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Busca as informações específicas de uma Arma no sistema (Ordem Paranormal).
        """
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Cadastra uma nova arma no sistema (Ordem Paranormal).
        **Disponível apenas para Admins.**
        """
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Atualiza as informações de uma arma especificada no sistema (Ordem Paranormal).
        **Disponível apenas para Admins.**
        """
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Remove uma arma especificada do sistema (Ordem Paranormal).
        **Disponível apenas para Admins.**
        """
        return super().destroy(request, *args, **kwargs)


class WeaponModViewSet(viewsets.ModelViewSet):
    queryset = WeaponMods.objects.all().order_by('id')
    serializer_class = WeaponModSerializer

    authentication_classes = (SessionAuthentication, TokenAuthentication)

    http_method_names = ['get', 'post', 'put', 'delete']

    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['weapon_name']
    filterset_class = WeaponModFilter

    def get_permissions(self):
        if self.action != "retrive" and self.action != "list":
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def list(self, request, *args, **kwargs):
        """
        Lista todas as Modificações para Armas no sistema (Ordem Paranormal).
        """
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Retorna os dados de uma Modificação para Arma especificada no sistema (Ordem Paranormal).
        """
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Cadastra uma nova Modificação para Arma no sistema (Ordem Paranormal).
        **Disponível apenas para Admins.**
        """
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        Atualiza os dados de uma Modificação para Arma especificada no sistema (Ordem Paranormal).
        **Disponível apenas para Admins.**
        """
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Remove uma Modificação para Arma especificada do sistema (Ordem Paranormal).
        **Disponível apenas para Admins.**
        """
        return super().destroy(request, *args, **kwargs)


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
