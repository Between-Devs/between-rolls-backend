from apps.login.views import *
from setup.urls import router
from django.urls import path

router.register('users', UserViewSet, 'Users')

urlpatterns = [
    path('login/', login, name='login'),
]