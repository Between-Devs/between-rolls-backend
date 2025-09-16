from rest_framework import serializers
from apps.character.models import *


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'


class AttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributes
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class OriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origin
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
    progression = serializers.ReadOnlyField(source='progression.progression')

    class Meta:
        model = Class
        fields = '__all__'


class SubclassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subclass
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'


class AvailableAbilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableAbilities
        fields = '__all__'


class AvailableRitualsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableRituals
        fields = '__all__'


class AvailableParanormalPowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableParanormalPowers
        fields = '__all__'


class ClassProgressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassProgression
        fields = '__all__'