from django_filters import rest_framework as filters
from .models import *

class WeaponFilter(filters.FilterSet):
    class Meta:
        model = Weapon
        fields = ['weapon_name', 'weapon_proficiency', 'weapon_type', 'weapon_category']


class WeaponModFilter(filters.FilterSet):
    class Meta:
        model = WeaponMods
        fields = ['modification', 'weapon_types']