from django_filters import rest_framework as filters
from .models import Weapon

class WeaponFilter(filters.FilterSet):
    
    class Meta:
        model = Weapon
        fields = ['weapon_name', 'weapon_proficiency', 'weapon_type', 'weapon_category']
