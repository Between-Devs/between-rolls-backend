from rest_framework import serializers
from apps.equipments.models import *


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = '__all__'


class WeaponModSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeaponMods
        fields = '__all__'


class AmmoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ammo
        fields = '__all__'


class ArmorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Armor
        fields = '__all__'


class ArmorModSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArmorMod
        fields = '__all__'


class GeneralEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralEquipment
        fields = '__all__'


class AccessoriesModSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessoriesMod
        fields = '__all__'


class ParanormalItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParanormalItens
        fields = '__all__' 
