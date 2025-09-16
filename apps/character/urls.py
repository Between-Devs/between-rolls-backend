from apps.character.views import *
from setup.urls import router

router.register('characters', CharacterViewSet, 'Characters')
router.register('attributes', AttributesViewSet, 'Attributes')
router.register('skills', SkillViewSet, 'Skills')
router.register('origins', OriginViewSet, 'Origins')
router.register('classes', ClassViewSet, 'Classes')
router.register('subclasses', SubclassViewSet, 'Subclasses')
router.register('inventory', InventoryViewSet, 'Inventory')
router.register('progression', ClassProgressionViewSet, 'Progression')

urlpatterns = [

]
