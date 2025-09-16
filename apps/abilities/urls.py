from apps.abilities.views import *
from setup.urls import router


router.register('abilities', AbilityViewSet, 'Abilities')
router.register('rituals', RitualsViewSet, 'Rituals')
router.register('paranormal-powers', ParanormalPowersViewSet, 'Paranormal Powers')

urlpatterns = [

]
