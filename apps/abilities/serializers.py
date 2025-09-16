from rest_framework import serializers
from apps.abilities.models import *


class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = '__all__'
        

class RitualsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rituals
        fields = '__all__'


class ParanormalPowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParanormalPowers
        fields = '__all__'
