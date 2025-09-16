from django.urls import path, include
from apps.equipments.views import *
from setup.urls import router

router.register('weapons', WeaponViewSet, 'Weapons')
router.register('weapons_mods', WeaponModViewSet, 'WeaponMods')
router.register('ammo', AmmoViewSet, 'Ammo')
router.register('armor', ArmorViewSet, 'Armor')
router.register('armor_mods', ArmorModViewSet, 'ArmorMods')
router.register('general_equipment', GeneralEquipmentViewSet, 'GeneralEquipment')
router.register('accessories_mods', AccessoriesModViewSet, 'AccessoriesMods')
router.register('paranormal_itens', ParanormalItensViewSet, 'ParanormalItens')

urlpatterns = [

]
